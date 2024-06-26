from .base_config import base_config
from copy import deepcopy

xgb_config = deepcopy(base_config)

xgb_config.model.model_class = "XGB"

xgb_config.model.fit_params["verbose"] = 0

xgb_config.model.additional_hparams["n_jobs"] = xgb_config.experiment.n_jobs
xgb_config.model.additional_hparams["enable_categorical"] = True
xgb_config.model.additional_hparams["early_stopping_rounds"] = xgb_config.experiment.early_stopping_patience

xgb_config.model.search_range = {
                                    'max_leaves' : ['suggest_int', ['max_leaves', 300, 4000]],
                                    'n_estimators' : ['suggest_int', ['n_estimators', 10, 3000]],
                                    'learning_rate' : ['suggest_float', ['learning_rate',0.001, 0.01]],
                                    'max_depth' : ['suggest_int', ['max_depth', 3, 20]],
                                    'scale_pos_weight' : ['suggest_int', ['scale_pos_weight', 3, 100]],
                                }