import requests                                                 
from bs4 import BeautifulSoup                                   
from PyQt5.QtWidgets import (QApplication, QWidget, QLineEdit, QPushButton,     
                                QComboBox, QVBoxLayout, QLabel)                 


n = 1
k = 1
text_n = ''

def active1(text):
    global n
    if text == 'dollar':
        n = 1
    elif text == 'euro':
        n = 2
    elif text == 'pound':
        n = 3
    elif text == 'canadian dollar':
        n = 4
    elif text == 'yuan':
        n = 5
    elif text == 'ruble':
        n = 6

def change(text):
    global text_n
    text_n = text 
    

def active2(text):
    global k
    if text == 'dollar':
        k = 1
    elif text == 'euro':
        k = 2
    elif text == 'pound':
        k = 3
    elif text == 'canadian dollar':
        k = 4
    elif text == 'yuan':
        k = 5
    elif text == 'ruble':
        k = 6

def but():
    coef = 0
    link = ''

    if n == 1:
        name1 = 'dollar'
        if k == 1:
            coef = 1
        elif k == 2:
            link = 'https://www.google.com/search?q=dollar+to+euro&biw=885&bih=821&ei=N88jYsaHMe-rrgSZt5GoCQ&ved=0ahUKEwiG_5TF7q_2AhXvlYsKHZlbBJUQ4dUDCA4&uact=5&oq=dollar+to+euro&gs_lcp=Cgdnd3Mtd2l6EAMyCggAEIAEEEYQggIyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgAEEcQsAM6BwgAELADEEM6BggAEBYQHjoKCAAQ6gIQtAIQQzoNCC4Q1AIQ6gIQtAIQQzoKCC4Q6gIQtAIQQzoECAAQQzoKCC4QxwEQ0QMQQzoRCC4QgAQQsQMQgwEQxwEQowI6DwguEIAEEMcBENEDEAoQAToLCAAQgAQQsQMQgwE6CggAELEDEIMBEEM6DggAEIAEELEDEIMBEMkDOg8IABCxAxCDARBDEEYQggI6BwgAEIAEEApKBAhBGABKBAhGGABQvQNYqUFg6EVoAnABeAGAAbgBiAHFFpIBBDcuMTmYAQCgAQGwAQrIAQrAAQE&sclient=gws-wiz'
        elif k == 3:
            link = 'https://www.google.com/search?q=dollar+to+pound&biw=885&bih=821&ei=s0wkYpiEDZLfrgSou4XQBw&ved=0ahUKEwjYqeaa5rD2AhWSr4sKHahdAXoQ4dUDCA4&uact=5&oq=dollar+to+pound&gs_lcp=Cgdnd3Mtd2l6EAMyCggAEIAEEEYQggIyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgAEEcQsAM6BwgAELADEEM6BAgAEEM6CQgAEEMQRhCCAjoHCAAQgAQQCjoLCAAQgAQQsQMQgwFKBAhBGABKBAhGGABQwwNYxhVg3hdoAXABeACAAXaIAaQHkgEDNC41mAEAoAEByAEKwAEB&sclient=gws-wiz'
        elif k == 4:
            link = 'https://www.google.com/search?q=dollar+to+canadian+dollar&biw=885&bih=821&ei=zEwkYsWXCIqGwPAPu8aS8AI&oq=dollar+to+cana&gs_lcp=Cgdnd3Mtd2l6EAEYADIKCAAQgAQQRhCCAjIFCAAQgAQyBQgAEIAEMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB46BwgAEEcQsAM6BwgAELADEEM6CggAEOQCELADGAA6EgguEMcBENEDEMgDELADEEMYAToECAAQQzoJCAAQQxBGEIICOgsIABCABBCxAxCDAToHCAAQgAQQCkoECEEYAEoECEYYAVDjBFjHE2CIHGgBcAF4AIABhAKIAZ8JkgEFNC4zLjKYAQCgAQHIARLAAQHaAQYIABABGAnaAQYIARABGAg&sclient=gws-wiz'
        elif k == 5:
            link = 'https://www.google.com/search?q=dollar+to+yuan&biw=885&bih=821&ei=4UwkYo_6EYSFwPAPn6GAmAw&ved=0ahUKEwjP7uKw5rD2AhWEAhAIHZ8QAMMQ4dUDCA4&uact=5&oq=dollar+to+yuan&gs_lcp=Cgdnd3Mtd2l6EAMyCggAEIAEEEYQggIyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgAEEcQsAM6BwgAELADEEM6Cw'
        elif k == 6:
            link = 'https://www.google.com/search?q=dollar+to+ruble&biw=885&bih=821&ei=8EwkYtiDD-z0qwGE4rKgCw&ved=0ahUKEwjYu_O35rD2AhVs-ioKHQSxDLQQ4dUDCA4&uact=5&oq=dollar+to+ruble&gs_lcp=Cgdnd3Mtd2l6EAMyEAgAEIAEELEDEIMBEEYQggIyCwgAEIAEELEDEIMBMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgAEEcQsAM6BwgAELADEEM6BAgAEEM6CQgAEEMQRhCCAjoHCAAQgAQQCkoECEEYAEoECEYYAFCZA1jSFmCcGmgBcAF4AIABd4gBhAeSAQM0LjWYAQCgAQHIAQrAAQE&sclient=gws-wiz'

    elif n == 2:
        name1 = 'euro'
        if k == 1:
            link = 'https://www.google.com/search?q=euro+to+dollar&biw=885&bih=821&ei=Ak0kYtOCIqL3qwH-uKjQBw&ved=0ahUKEwjTi9HA5rD2AhWi-yoKHX4cCnoQ4dUDCA4&uact=5&oq=euro+to+dollar&gs_lcp=Cgdnd3Mtd2l6EAMyDwgAELEDEIMBEEMQRhCCAjIFCAAQgAQyBAgAEEMyBQgAEIAEMgQIABBDMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6CggAEOoCELQCEEM6DQguENQCEOoCELQCEEM6CwgAEIAEELEDEIMBOggIABCxAxCDAToLCC4QgAQQsQMQgwE6CAgAEIAEELEDOhEILhCABBCxAxCDARDHARCjAjoKCAAQsQMQgwEQQ0oECEEYAEoECEYYAFAAWOUiYP4jaAFwAXgCgAHZBIgBuhSSAQsyLjcuMi4wLjEuMZgBAKABAbABCsABAQ&sclient=gws-wiz'
        elif k == 2:
            coef = 1
        elif k == 3:
            link = 'https://www.google.com/search?q=euro+to+pound&biw=885&bih=821&ei=Q00kYsb2EMeyrgS0jpaABg&ved=0ahUKEwiGpL_f5rD2AhVHmYsKHTSHBWAQ4dUDCA4&uact=5&oq=euro+to+pound&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOgcIABBHELADOgcIABCwAxBDOgoIABCxAxCDARBDOg8IABCxAxCDARBDEEYQggI6CwgAEIAEELEDEIMBOgQIABBDOgcIABCABBAKSgQIQRgASgQIRhgAULgDWPQdYIYhaAFwAXgAgAGAAYgBjQiSAQM3LjSYAQCgAQHIAQrAAQE&sclient=gws-wiz'
        elif k == 4:
            link = 'https://www.google.com/search?q=euro+to+canadian+dollar&biw=885&bih=821&ei=XE0kYvifMe7lrgSHnqrwAw&oq=euro+to+canadi&gs_lcp=Cgdnd3Mtd2l6EAEYADIKCAAQgAQQRhCCAjIFCAAQgAQyBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeOgcIABBHELADOgcIABCwAxBDOhIILhDHARDRAxDIAxCwAxBDGAA6EgguEMcBEKMCEMgDELADEEMYADoECAAQQzoJCAAQQxBGEIICOgcIABCABBAKOgsIABCABBCxAxCDAUoECEEYAEoECEYYAFCJA1i_FmCXIWgBcAF4AIABmwGIAb8IkgEDNy40mAEAoAEByAELwAEB2gEECAAYCA&sclient=gws-wiz'
        elif k == 5:
            link = 'https://www.google.com/search?q=euro+to+yuan&biw=885&bih=821&ei=bE0kYr-IIMv1qwGb16HQCg&ved=0ahUKEwi_7pTz5rD2AhXL-ioKHZtrCKoQ4dUDCA4&uact=5&oq=euro+to+yuan&gs_lcp=Cgdnd3Mtd2l6EAMyCggAEIAEEEYQggIyBQgAEIAEMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjoHCAAQRxCwAzoHCAAQsAMQQzoKCAAQ5AIQsAMYADoSCC4QxwEQ0QMQyAMQsAMQQxgBOgwILhDIAxCwAxBDGAE6FQguEMcBENEDENQCEMgDELADEEMYAToPCC4Q1AIQyAMQsAMQQxgBOgQIABBDOgsIABCABBCxAxCDAToKCAAQsQMQgwEQQzoKCAAQsQMQgwEQCjoECAAQCjoICAAQFhAKEB5KBAhBGABKBAhGGAFQ9wRYjhNggRZoAXABeACAAXeIAYcEkgEDMi4zmAEAoAEByAETwAEB2gEGCAAQARgJ2gEGCAEQARgI&sclient=gws-wiz'
        elif k == 6:
            link = 'https://www.google.com/search?q=euro+to+ruble&biw=885&bih=821&ei=e00kYvnKEqGEwPAPhcyviAo&ved=0ahUKEwi59Jr65rD2AhUhAhAIHQXmC6EQ4dUDCA4&uact=5&oq=euro+to+ruble&gs_lcp=Cgdnd3Mtd2l6EAMyEAgAEIAEELEDEIMBEEYQggIyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgAEEcQsAM6BwgAELADEEM6CwgAEIAEELEDEIMBSgQIQRgASgQIRhgAULYDWNoVYLcaaAFwAXgBgAHxBIgB0BKSAQsxLjIuMy4xLjEuMZgBAKABAcgBCsABAQ&sclient=gws-wiz'

    elif n == 3:
        name1 = 'pound'
        if k == 1:
            link = 'https://www.google.com/search?q=pound+to+dollar&biw=885&bih=821&ei=ik0kYoqKELKHwPAPtp2BqAk&ved=0ahUKEwiK96uB57D2AhWyAxAIHbZOAJUQ4dUDCA4&uact=5&oq=pound+to+dollar&gs_lcp=Cgdnd3Mtd2l6EAMyCQgAEEMQRhCCAjIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoHCAAQRxCwAzoHCAAQsAMQQzoSCC4QxwEQowIQyAMQsAMQQxgAOhIILhDHARDRAxDIAxCwAxBDGAA6CggAEOoCELQCEEM6DAgAEOoCELQCEAoQQzoNCC4Q1AIQ6gIQtAIQQzoQCC4QsQMQgwEQxwEQ0QMQQzoECAAQQzoICAAQsQMQgwE6BAguEEM6EQguEIAEELEDEIMBEMcBEKMCOgsIABCABBCxAxCDAToPCAAQsQMQgwEQQxBGEIICOggIABCABBCxAzoOCC4QgAQQsQMQgwEQ1AJKBAhBGABKBAhGGABQpwNY7TdgkjloAnABeACAAc8BiAGhDZIBBTYuOC4xmAEAoAEBsAEKyAEMwAEB2gEECAAYCA&sclient=gws-wiz'
        elif k == 2:
            link = 'https://www.google.com/search?q=pound+to+euro&biw=885&bih=821&ei=wU0kYpysGaKWjgapsaPgAw&ved=0ahUKEwjckNKb57D2AhUii8MKHanYCDwQ4dUDCA4&uact=5&oq=pound+to+euro&gs_lcp=Cgdnd3Mtd2l6EAMyCggAEIAEEEYQggIyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BwgAEEcQsAM6BwgAELADEEM6CwgAEIAEELEDEIMBOggIABCABBCxA0oECEEYAEoECEYYAFDjAlibGGDZG2gBcAF4AIABdogB3AeSAQM0LjaYAQCgAQHIAQrAAQE&sclient=gws-wiz'
        elif k == 3:
            coef = 1
        elif k == 4:
            link = 'https://www.google.com/search?q=pound+to+canadian+dollar&biw=885&bih=821&ei=zk0kYsqiHKWtrgT0lKawCw&oq=pound+to+ca&gs_lcp=Cgdnd3Mtd2l6EAEYATIFCAAQgAQyBQgAEIAEMgUIABCABDIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeOgcIABBHELADOgcIABCwAxBDOgoIABDkAhCwAxgAOhIILhDHARDRAxDIAxCwAxBDGAE6BAgAEEM6CQgAEEMQRhCCAjoLCAAQgAQQsQMQgwE6CAgAEIAEELEDSgQIQRgASgQIRhgBUJ8DWIwOYMsfaAFwAXgAgAFziAG1BJIBAzQuMpgBAKABAcgBE8ABAdoBBggAEAEYCdoBBggBEAEYCA&sclient=gws-wiz'
        elif k == 5:
            link = 'https://www.google.com/search?q=pound+to+yuan&biw=885&bih=821&ei=300kYtngFcSr3AOc1KS4DQ&ved=0ahUKEwiZzPWp57D2AhXEFXcKHRwqCdcQ4dUDCA4&uact=5&oq=pound+to+yuan&gs_lcp=Cgdnd3Mtd2l6EAMyCggAEIAEEEYQggIyBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB46BwgAEEcQsAM6BwgAELADEEM6CggAEOQCELADGAA6EgguEMcBENEDEMgDELADEEMYAToSCC4QxwEQowIQyAMQsAMQQxgBOgUIABCABDoECAAQQzoLCAAQgAQQsQMQgwE6CAgAEIAEELEDOggIABAWEAoQHjoJCAAQyQMQFhAeSgQIQRgASgQIRhgBUIAEWI4sYI0vaAFwAXgAgAGKAYgBlRCSAQQ3LjEymAEAoAEByAETwAEB2gEGCAAQARgJ2gEGCAEQARgI&sclient=gws-wiz'
        elif k == 6:
            link = 'https://www.google.com/search?q=pound+to+ruble&biw=885&bih=821&ei=8U0kYsmaAuGkrgSgsIjwBQ&ved=0ahUKEwiJ16yy57D2AhVhkosKHSAYAl4Q4dUDCA4&uact=5&oq=pound+to+ruble&gs_lcp=Cgdnd3Mtd2l6EAMyCggAEMQCEEYQggIyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeOgcIABBHELADOgcIABCwAxBDOgkIABDJAxAWEB46CggAEIAEEEYQggI6CAgAEBYQChAeOgQIABBDOgsIABCABBCxAxCDAToICAAQgAQQsQM6EAgAEIAEELEDEIMBEEYQggJKBAhBGABKBAhGGABQ_QJY2BVg9xdoAXABeACAAYoBiAHWB5IBAzQuNZgBAKABAcgBCsABAQ&sclient=gws-wiz'

    elif n == 4:
        name1 = 'canadian'
        if k == 1:
            link = 'https://www.google.com/search?q=canadian+to+dollarr&biw=885&bih=821&ei=Ak0kYtOCIqL3qwH-uKjQBw&ved=0ahUKEwjTi9HA5rD2AhWi-yoKHX4cCnoQ4dUDCA4&uact=5&oq=canadian+to+dollarr&gs_lcp=Cgdnd3Mtd2l6EAMyCggAEIAEEEYQggIyBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB46CggAEOoCELQCEEM6DQguENQCEOoCELQCEEM6CwgAEIAEELEDEIMBOhEILhCABBCxAxCDARDHARDRAzoLCC4QgAQQxwEQowI6CwguEIAEEMcBENEDOhEILhCABBCxAxCDARDHARCjAjoOCC4QgAQQsQMQxwEQ0QM6CwguELEDEIMBENQCOgQIABBDOgoILhDHARCjAhBDOgcIABCxAxBDOgkIABBDEEYQggI6FAguEIAEELEDEIMBEMcBEKMCENQCOgUIABCABDoLCC4QgAQQsQMQ1AI6DgguEIAEELEDEMcBEKMCOgQIABAKOgsILhCABBDHARCvAUoECEEYAEoECEYYAFAAWJs9YKI9aAFwAXgAgAHCAYgBnBCSAQQzLjE1mAEAoAEBsAEKwAEB&sclient=gws-wiz'
        elif k == 2:
            link = 'https://www.google.com/search?q=canadian+to+euro&biw=885&bih=821&ei=L04kYt3ICujjrgS-mJmoAg&ved=0ahUKEwidnP3P57D2AhXosYsKHT5MBiUQ4dUDCA4&uact=5&oq=canadian+to+euro&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeOgQIABBHOgoIABCABBBGEIICSgQIQRgASgUIQBIBMUoECEYYAFC7A1iBKGCrK2gAcAJ4AIABeYgB8weSAQM1LjWYAQCgAQHIAQjAAQE&sclient=gws-wiz'
        elif k == 3:
            link = 'https://www.google.com/search?q=canadian+to+pound&biw=885&bih=821&ei=8U4kYvK4MoSarwTk153QAQ&ved=0ahUKEwiy9eWs6LD2AhUEzYsKHeRrBxoQ4dUDCA4&uact=5&oq=canadian+to+pound&gs_lcp=Cgdnd3Mtd2l6EAMyBAgAEBMyBAgAEBMyBAgAEBMyBAgAEBMyBAgAEBMyBAgAEBMyBAgAEBMyBAgAEBMyBAgAEBMyCAgAEBYQHhATOgcIABBHELADOgcIABCwAxBDOgUIABCABDoECAAQQzoGCAAQFhAeOgoIABCABBBGEIICSgQIQRgASgQIRhgAUIcDWKUoYJgraAFwAXgAgAGFAYgByQeSAQMyLjeYAQCgAQHIAQrAAQE&sclient=gws-wiz'
        elif k == 4:
            coef = 1
        elif k == 5:
            link = 'https://www.google.com/search?q=canadian+to+yuan&biw=885&bih=821&ei=Ak8kYsWYJpeVrwTG67PYDA&ved=0ahUKEwjFoee06LD2AhWXyosKHcb1DMsQ4dUDCA4&uact=5&oq=canadian+to+yuan&gs_lcp=Cgdnd3Mtd2l6EAMyBAgAEBMyCAgAEBYQHhATMggIABAWEB4QEzIICAAQFhAeEBMyCAgAEBYQHhATMggIABAWEB4QEzIICAAQFhAeEBM6BwgAEEcQsAM6BwgAELADEEM6BQgAEIAEOgYIABAKEBM6BggAEBYQHjoICAAQFhAKEB5KBAhBGABKBAhGGABQ7wRYoRtg-x5oAXABeACAAX-IAcsHkgEDMi43mAEAoAEByAEKwAEB&sclient=gws-wiz'
        elif k == 6:
            link = 'https://www.google.com/search?q=canadian+to+ruble&biw=885&bih=821&ei=EE8kYuz5Gcn5qwHyqqS4BA&ved=0ahUKEwjswbG76LD2AhXJ_CoKHXIVCUcQ4dUDCA4&uact=5&oq=canadian+to+ruble&gs_lcp=Cgdnd3Mtd2l6EAMyCggAEIAEEEYQggIyBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB46BwgAEEcQsAM6CAgAEBYQChAeOgQIABATOgYIABAKEBM6CAgAEBYQHhATOgUIABCABEoECEEYAEoECEYYAFDgAljcFWDmF2gBcAF4AIABcogB0gaSAQM2LjOYAQCgAQHIAQjAAQE&sclient=gws-wiz'

    elif n == 5:
        name1 = 'yuan'
        if k == 1:
            link = 'https://www.google.com/search?q=yuan+to+dollar&biw=885&bih=821&ei=Hk8kYs_TB47brgS44bSwBQ&ved=0ahUKEwjP2vXB6LD2AhWOrYsKHbgwDVYQ4dUDCA4&uact=5&oq=yuan+to+dollar&gs_lcp=Cgdnd3Mtd2l6EAMyCggAEIAEEEYQggIyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjoRCAAQ6gIQtAIQigMQtwMQ5QI6FAgAEOoCELQCEIoDELcDENQDEOUCOhEILhCABBCxAxCDARDHARDRAzoJCAAQgAQQChABOgsIABCABBCxAxCDAToICAAQgAQQsQM6BAgAEEM6CAguEIAEELEDOhEILhCABBCxAxCDARDHARCvAToJCAAQQxBGEIICOgcIABCABBAKOhAILhCxAxCDARDHARDRAxAKOgUILhCABDoGCAAQChAqOggIABAWEAoQHkoECEEYAEoECEYYAFAAWM8xYMozaAJwAXgAgAGDAYgBngySAQQ1LjEwmAEAoAEBsAEKwAEB&sclient=gws-wiz'
        elif k == 2:
            link = 'https://www.google.com/search?q=yuan+to+euro&biw=885&bih=821&ei=N08kYpTdPITfrgTS6YaoBw&ved=0ahUKEwjU1KDO6LD2AhWEr4sKHdK0AXUQ4dUDCA4&uact=5&oq=yuan+to+euro&gs_lcp=Cgdnd3Mtd2l6EAMyCggAEIAEEEYQggIyBQgAEIAEMgUIABCABDIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeOgcIABBHELADOgcIABCwAxBDOgQIABBDOgkIABBDEEYQggI6CAgAEBYQChAeOgsIABCABBCxAxCDAUoECEEYAEoECEYYAFDoA1iWG2ChHmgBcAF4AIABbYgBsgeSAQM2LjSYAQCgAQHIAQrAAQE&sclient=gws-wiz'
        elif k == 3:
            link = 'https://www.google.com/search?q=yuan+to+pound&biw=885&bih=821&ei=RE8kYofPM-jjrgS-mJmoAg&ved=0ahUKEwiHgbHU6LD2AhXosYsKHT5MBiUQ4dUDCA4&uact=5&oq=yuan+to+pound&gs_lcp=Cgdnd3Mtd2l6EAMyCggAEIAEEEYQggIyBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB46BwgAEEcQsAM6BwgAELADEEM6EgguEMcBENEDEMgDELADEEMYADoMCC4QyAMQsAMQQxgAOgQIABBDOgUIABCABDoJCAAQQxBGEIICOgsIABCABBCxAxCDAToICAAQFhAKEB5KBAhBGABKBAhGGABQygJY7xZg7hloAXABeACAAXSIAecGkgEDNS40mAEAoAEByAELwAEB2gEECAAYCA&sclient=gws-wiz'
        elif k == 4:
            link = 'https://www.google.com/search?q=yuan+to+canadian+dollars&biw=885&bih=821&ei=Uk8kYoKYK8Wgjgb825L4Bg&oq=yuan+to+cana&gs_lcp=Cgdnd3Mtd2l6EAEYATIECAAQEzIECAAQEzIECAAQEzIECAAQEzIECAAQEzIECAAQEzIICAAQFhAeEBMyCAgAEBYQHhATMggIABAWEB4QEzIICAAQFhAeEBM6BwgAEEcQsAM6BwgAELADEEM6BQgAEIAEOgYIABAWEB46CggAEIAEEEYQggI6CQgAEEMQRhCCAjoICAAQFhAKEB46CwgAEIAEELEDEIMBOgQIABBDSgQIQRgASgQIRhgAUPMDWIoTYJobaAFwAXgAgAF3iAHoBpIBAzUuNJgBAKABAcgBCsABAQ&sclient=gws-wiz'
        elif k == 5:
            coef = 1
        elif k == 6:
            link = 'https://www.google.com/search?q=yuan+to+rub&biw=885&bih=821&ei=YE8kYuKnC4mcrgSksYAQ&oq=yuan+to+&gs_lcp=Cgdnd3Mtd2l6EAEYADIQCAAQgAQQsQMQgwEQRhCCAjIFCAAQgAQyBQgAEIAEMgUIABCABDIECAAQQzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOgcIABBHELADOgsIABCABBCxAxCDAToICAAQFhAKEB46BggAEBYQHkoECEEYAEoECEYYAFDpA1iaEmCSHGgCcAF4AIABbYgBuwKSAQMwLjOYAQCgAQHIAQfAAQE&sclient=gws-wiz'
    
    elif n == 6:
        name1 = 'ruble'
        if k == 1:
            link = 'https://www.google.com/search?q=ruble+to+doolar&biw=885&bih=821&ei=cU8kYsynFYz7rgTqpZWIBg&ved=0ahUKEwiMpM3p6LD2AhWMvYsKHepSBWEQ4dUDCA4&uact=5&oq=ruble+to+doolar&gs_lcp=Cgdnd3Mtd2l6EAMyDwgAELEDEIMBEAoQRhCCAjIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjoKCAAQ6gIQtAIQQzoUCAAQ6gIQtAIQigMQtwMQ1AMQ5QI6EQgAEOoCELQCEIoDELcDEOUCOgQIABBDOgsIABCABBCxAxCDAToRCC4QgAQQsQMQgwEQxwEQowI6EQguEIAEELEDEIMBEMcBENEDOgkIABBDEEYQggI6CggAELEDEIMBEEM6CAgAELEDEIMBOg8IABCxAxCDARBDEEYQggI6BQgAEIAEOhAIABCABBCxAxCDARBGEIICSgQIQRgASgQIRhgAUABYky9grDBoAXABeACAAZABiAHZDJIBBDMuMTKYAQCgAQGwAQrAAQE&sclient=gws-wiz'
        elif k == 2:
            link = 'https://www.google.com/search?q=ruble+to+euro&biw=885&bih=821&ei=iE8kYuitHI2EwPAPndmvsAI&ved=0ahUKEwjokdD06LD2AhUNAhAIHZ3sCyYQ4dUDCA4&uact=5&oq=ruble+to+euro&gs_lcp=Cgdnd3Mtd2l6EAMyCggAEMQCEEYQggIyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeOgQIABBHOgoIABCxAxCDARBDOg8IABCxAxCDARBDEEYQggI6CwgAEIAEELEDEIMBOhAIABCABBCxAxCDARBGEIICSgQIQRgASgUIQBIBMUoECEYYAFDQAljDG2C_IGgAcAJ4AIABeYgBqAeSAQM5LjGYAQCgAQHIAQjAAQE&sclient=gws-wiz'
        elif k == 3:
            link = 'https://www.google.com/search?q=ruble+to+pound&biw=885&bih=821&ei=o08kYuTYJe2ArwTw3I6gCA&ved=0ahUKEwiktsmB6bD2AhVtwIsKHXCuA4QQ4dUDCA4&uact=5&oq=ruble+to+pound&gs_lcp=Cgdnd3Mtd2l6EAMyCggAEIAEEEYQggIyBQgAEIAEMgUIABCABDIFCAAQgAQyBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB46BwgAEEcQsAM6BwgAELADEEM6CggAELEDEIMBEEM6DwgAELEDEIMBEEMQRhCCAjoLCAAQgAQQsQMQgwFKBAhBGABKBAhGGABQ3QJYiyVgiihoAnABeACAAXCIAYUHkgEDOC4ymAEAoAEByAEKwAEB&sclient=gws-wiz'
        elif k == 4:
            link = 'https://www.google.com/search?q=ruble+to+canadian+dollar&biw=885&bih=821&ei=sk8kYvf8G_DnrgSAg4jwDg&oq=ruble+to+cana&gs_lcp=Cgdnd3Mtd2l6EAEYADIFCAAQgAQyBQgAEIAEMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjoHCAAQRxCwAzoHCAAQsAMQQzoKCAAQ5AIQsAMYADoSCC4QxwEQ0QMQyAMQsAMQQxgBOg8ILhDUAhDIAxCwAxBDGAE6BAgAEEM6CQgAEEMQRhCCAjoLCAAQgAQQsQMQgwE6CggAEIAEEEYQggJKBAhBGABKBAhGGAFQ5AJY4C5gjDVoAXABeACAAXWIAd0GkgEDNy4ymAEAoAEByAESwAEB2gEGCAAQARgJ2gEGCAEQARgI&sclient=gws-wiz'
        elif k == 5:
            link = 'https://www.google.com/search?q=ruble+to+yuan&biw=885&bih=821&ei=xU8kYtGrPOahrgSv4rrABQ&ved=0ahUKEwiRovuR6bD2AhXmkIsKHS-xDlgQ4dUDCA4&uact=5&oq=ruble+to+yuan&gs_lcp=Cgdnd3Mtd2l6EAMyCggAEIAEEEYQggIyBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB46BwgAEEcQsAM6BQgAEIAEOgQIABBDOgsIABCABBCxAxCDAToKCAAQsQMQgwEQCjoECAAQCkoECEEYAEoECEYYAFCoA1ihH2CCImgBcAF4AIABc4gB4A6SAQQ5LjEwmAEAoAEByAEIwAEB&sclient=gws-wiz'
        elif k == 6:
            coef = 1
    
    if coef == 1:
        text3.setText(text_n)
    
    elif k != 6 and n == 6:
        if k == 1 or k == 4 or k == 5:
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}
            full_page1 = requests.get(link, headers=headers)
            soup1 = BeautifulSoup(full_page1.content, 'html.parser')
            convert1 = soup1.find_all("span", {'class': 'DFlfde SwHCTb', 'data-precision': "3"})

        elif k == 2 or k == 3:
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}
            full_page1 = requests.get(link, headers=headers)
            soup1 = BeautifulSoup(full_page1.content, 'html.parser')
            convert1 = soup1.find_all("span", {'class': 'DFlfde SwHCTb', 'data-precision': "4"})
        
        if ',' in convert1[0].text:
            coef = float(convert1[0].text.replace(',', '.'))
        else:
            coef = float(convert1[0].text)
        num = float(text_n) * coef

        text3.setText(str(num))

    else:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}
        full_page1 = requests.get(link, headers=headers)
        soup1 = BeautifulSoup(full_page1.content, 'html.parser')
        convert1 = soup1.find_all("span", {'class': 'DFlfde SwHCTb', 'data-precision': "2"})
        
        if ',' in convert1[0].text:
            coef = float(convert1[0].text.replace(',', '.'))
        else:
            coef = float(convert1[0].text)
        num = round(float(text_n) * coef, 3)

        text3.setText(str(num))

    if k == 1:
        name2 = 'dollar'
    elif k == 2:
        name2 = 'euro'
    elif k == 3:
        name2 = 'pound'
    elif k == 4:
        name2 = 'canadian'
    elif k == 5:
        name2 = 'yuan'
    elif k == 6:
        name2 = 'ruble'
        
    text = '1 ' + name1 + ' = ' + str(coef) + ' ' + name2
    text_1.setText(text)
    

app = QApplication([])
wind = QWidget()
wind.setWindowTitle('Converter')

list1 = QComboBox()
list2 = QComboBox()

list_val = ['dollar', 'euro', 'pound', 'canadian dollar', 'yuan', 'ruble']

for i in list_val:
    list1.addItem(i)
    list2.addItem(i)

text_1 = QLabel('1 dollar = 1 dollar')
text1 = QLineEdit()
but1 = QPushButton('Change')
text3 = QLabel('Amount')

line = QVBoxLayout()
line.addWidget(text_1)
line.addWidget(list1)
line.addWidget(text1)
line.addWidget(list2)
line.addWidget(text3)       
line.addWidget(but1)


list1.activated[str].connect(active1)
list2.activated[str].connect(active2)
text1.textEdited.connect(change)
but1.clicked.connect(but)


wind.setLayout(line)


wind.show()
app.exec_()
