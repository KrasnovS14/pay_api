from main import app

@app.post('/add-user-card')
async def add_user_card_api(user_id: int, cardholder:str,  card_number: int, exp_date: int, opt: int):
    pass


# Генерация проверочного кода
@app.get('/one-time-password')
async def get_one_time_password(transfer_id: int):
    pass

# перевод денег
@app.post('/transfer-user-money')
async def transfer_money_api(card_from: int, card_to: int, otp: int):
    pass



# удаление карты
@app.delete('/delete-user-card')
async def delete_user_card(card_id: int, user_id: int):
    pass


# Вывод карту
@app.get('/get-user-cards')
async def get_exact_of_all_cards(user_id: int, card: int = 0):
    pass


# Вывод истории карту
@app.get('/get-cards-monitoring')
async def get_exact_of_all_cards_monitoring(card: int = 0):
    pass