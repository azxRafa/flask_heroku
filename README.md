# flask_heroku
1. Электив первый:
- Предсказание
    
    POST [`https://site/api/predict`](https://site/api/predict)
    
    {по данным из датасета}
    
    POST [`https://site/api/model_name/predict`](https://site/api/model_name/predict)
    
    {по данным из датасета}
    
- Список моделей.
    
    GET [`https://site/api/model`](https://site/api/model)
    
    возращать должен
    
    [{"model_name":"model1",
    "desc": "Какое то описание модели"}]
