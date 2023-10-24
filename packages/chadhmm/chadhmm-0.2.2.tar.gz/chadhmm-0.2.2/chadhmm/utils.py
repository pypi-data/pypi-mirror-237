import torch
from typing import Sequence, Tuple, Optional
from prettytable import PrettyTable

class ConvergenceHandler:
    """
    Convergence Monitor
    ----------
    Convergence monitor for HMM training. Stores the score at each iteration and checks for convergence.

    Parameters
    ----------
    max_iter : int
        Maximum number of iterations.
    n_init : int
        Number of initializations.
    tol : float
        Convergence threshold.
    post_conv_iter : int
        Number of iterations to run after convergence.
    verbose : bool
        Print convergence information.
    """

    def __init__(self, 
                 max_iter: int,
                 n_init:int , 
                 tol: float, 
                 post_conv_iter: int,
                 device: torch.device, 
                 verbose: bool = True):
        
        self.tol: float = tol
        self.verbose: bool = verbose
        self.post_conv_iter: int = post_conv_iter
        self.device: torch.device = device
        self.iter: int = 0
        self.score = torch.full(size=(max_iter, n_init),
                                fill_value=float('nan'), 
                                dtype=torch.float64,
                                device=self.device)
                                
        self.delta = self.score.clone()
        
    def _update(self, new_score: float, rank: int):
        """Update the iteration count."""
        old_score = self.score[self.iter-1, rank]
        self.score[self.iter, rank] = new_score
        self.delta[self.iter, rank] = new_score - old_score

    def check(self, new_score: float, rank: int) -> bool:
        """Check if the model has converged and update the convergence monitor."""    
        # Store prev score and update current score
        self._update(new_score, rank)

        # Update iteration count and check convergence
        if self.iter < self.post_conv_iter:
            is_converged = False
        else:
            is_converged = bool(torch.all(self.delta[(self.iter-self.post_conv_iter):self.iter, rank] < self.tol).item())

        # Print convergence information
        if self.verbose:
            print(f"""Iteration: {self.iter+1} | Score: {new_score:.2f} | Delta: {self.delta[self.iter, rank].item():.2f} | Converged = {is_converged}""")            

        return is_converged

def states_names(n: int, state_type: str) -> Sequence[str]:
    type_alias = state_type[0].upper()
    return [f'{type_alias}_{n}' for n in range(n)]

def laplace_smoothing(log_matrix: torch.Tensor, k: float) -> torch.Tensor:
    """Laplace smoothing of a log probability matrix"""

    if k <= 0.0:  
        return log_matrix
    else:
        real_matrix = torch.exp(log_matrix) 
        smoothed_log_matrix = torch.log((real_matrix + k) / (1 + k * real_matrix.shape[-1]))
        return smoothed_log_matrix
    
def init_matrix(prior: float, target_size: Tuple[int], semi: bool = False) -> torch.Tensor:
    
    alphas = torch.full(size=target_size, 
                        fill_value=prior, 
                        dtype=torch.float64)
    
    probs = torch.distributions.Dirichlet(alphas).sample()

    if semi:
        probs.fill_diagonal_(0)
        probs /= probs.sum(dim=-1, keepdim=True)

    return probs

def validate_means(means: torch.Tensor, n_states: int, n_features: int, n_components: Optional[int]=None) -> torch.Tensor:
    """Do basic checks on matrix mean sizes and values"""
    if n_components is None:
        valid_shape = (n_states, n_features)
        if (n_dim:=means.ndim) != 2:
            raise ValueError(f"Tensor must be 2D, got {n_dim} dims instead")
        elif (m_shape:=means.shape) != valid_shape:
            raise ValueError(f"Tensor must have shape {valid_shape}, got {m_shape} instead")
    else:
        valid_shape = (n_states, n_components, n_features)
        if (n_dim:=means.ndim) != 3:
            raise ValueError(f"Tensor must be 3D, got {n_dim} dims instead")
        elif (m_shape:=means.shape) != valid_shape:
            raise ValueError(f"Tensor must have shape {valid_shape}, got {m_shape} instead")

    if torch.any(torch.isnan(means)):
        raise ValueError("means must not contain NaNs")
    elif torch.any(torch.isinf(means)):
        raise ValueError("means must not contain infinities")
    else:
        return means
    
def validate_lambdas(lambdas: torch.Tensor, n_states: int, n_features: int) -> torch.Tensor:
    """Do basic checks on matrix mean sizes and values"""
    
    if len(lambdas.shape) != 2:
        raise ValueError("lambdas must have shape (n_states, n_features)")
    elif lambdas.shape[0] != n_states:
        raise ValueError("lambdas must have shape (n_states, n_features)")
    elif lambdas.shape[1] != n_features:
        raise ValueError("lambdas must have shape (n_states, n_features)")
    elif torch.any(torch.isnan(lambdas)):
        raise ValueError("lambdas must not contain NaNs")
    elif torch.any(torch.isinf(lambdas)):
        raise ValueError("lambdas must not contain infinities")
    elif torch.any(lambdas <= 0):
        raise ValueError("lambdas must be positive")
    else:
        return lambdas

def validate_covars(covars: torch.Tensor, 
                    covariance_type: str, 
                    n_states: int, 
                    n_features: int,
                    n_components: Optional[int]=None) -> torch.Tensor:
    """Do basic checks on matrix covariance sizes and values"""
    if n_components is None:
        valid_shape = torch.Size((n_states, n_features, n_features))
    else:
        valid_shape = torch.Size((n_states, n_components, n_features, n_features))    

    if covariance_type == 'spherical':
        if len(covars) != n_features:
            raise ValueError("'spherical' covars have length n_features")
        elif torch.any(covars <= 0): 
            raise ValueError("'spherical' covars must be positive")
    elif covariance_type == 'tied':
        if covars.shape[0] != covars.shape[1]:
            raise ValueError("'tied' covars must have shape (n_dim, n_dim)")
        elif (not torch.allclose(covars, covars.T) or torch.any(covars.symeig(eigenvectors=False).eigenvalues <= 0)):
            raise ValueError("'tied' covars must be symmetric, positive-definite")
    elif covariance_type == 'diag':
        if len(covars.shape) != 2:
            raise ValueError("'diag' covars must have shape (n_features, n_dim)")
        elif torch.any(covars <= 0):
            raise ValueError("'diag' covars must be positive")
    elif covariance_type == 'full':
        if len(covars.shape) != 3:
            raise ValueError("'full' covars must have shape (n_features, n_dim, n_dim)")
        elif covars.shape[1] != covars.shape[2]:
            raise ValueError("'full' covars must have shape (n_features, n_dim, n_dim)")
        for n, cv in enumerate(covars):
            eig_vals, _ = torch.linalg.eigh(cv)
            if (not torch.allclose(cv, cv.T) or torch.any(eig_vals <= 0)):
                raise ValueError(f"component {n} of 'full' covars must be symmetric, positive-definite")
    else:
        raise NotImplementedError(f"This covariance type is not implemented: {covariance_type}")
    
    return covars
       
def init_covars(tied_cv: torch.Tensor, 
                covariance_type: str, 
                n_states: int) -> torch.Tensor:
    """Initialize covars to a given covariance type"""

    if covariance_type == 'spherical':
        return tied_cv.mean() * torch.ones((n_states,))
    elif covariance_type == 'tied':
        return tied_cv
    elif covariance_type == 'diag':
        return tied_cv.diag().unsqueeze(0).expand(n_states, -1)
    elif covariance_type == 'full':
        return tied_cv.unsqueeze(0).expand(n_states, -1, -1)
    else:
        raise NotImplementedError(f"This covariance type is not implemented: {covariance_type}")
    
def fill_covars(covars: torch.Tensor, 
                covariance_type: str, 
                n_states: int, 
                n_features: int,
                n_components: Optional[int]=None) -> torch.Tensor:
    """Fill in missing values for covars"""
    
    if covariance_type == 'full':
        return covars
    elif covariance_type == 'diag':
        return torch.stack([torch.diag(covar) for covar in covars])
    elif covariance_type == 'tied':
        return covars.unsqueeze(0).expand(n_states, -1, -1)
    elif covariance_type == 'spherical':
        eye = torch.eye(n_features).unsqueeze(0)
        return eye * covars.unsqueeze(-1).unsqueeze(-1)
    else:
        raise NotImplementedError(f"This covariance type is not implemented: {covariance_type}")

def print_table(rows: list, header: list, title: str):
    """
    Helper method for the pretty print function. It prints the parameters
    as a nice table.
    """
    t = PrettyTable(title=title, 
                    field_names=header, 
                    header_style='upper',
                    padding_width=1, 
                    title_style='upper')
    
    for row in rows:
        t.add_row(row)
    
    print(t)