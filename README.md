1. Программа на Python, которая в реальном времени считывает текущую цену фьючерса XRP/USDT на бирже Binance. 
В случае, если цена упала на 1% от максимальной цены за последний час, программа выводит сообщение в консоль. 
При этом программа продолжает работать дальше, постоянно считывая актуальную цену.
Программа работает через вебсокеты, url: [wss://stream.binance.com:9443/ws/xrpusdt@ticker_1h](wss://stream.binance.com:9443/ws/xrpusdt@ticker_1h).
Период обновления, согласно binance api - 1000мс.

2. Для того, чтобы программа работала со всеми парами нужно изменить url на [wss://stream.binance.com:9443/ws/!ticker_1h@arr](wss://stream.binance.com:9443/ws/!ticker_1h@arr).
В ответе будет список, с парами, где произошли изменения за последний час. Вместо вызова функции `check_drop()` в функции `on_message()`, надо будет пройтись циклом по элементам списка с парами. И для каждого элемента вызвать функцию `check_drop()`.