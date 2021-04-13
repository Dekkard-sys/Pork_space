from tkinter import *


def second_window_open():
    def third_window_open():
        def fourth_window_open():
            def fifth_window_open():
                def sixth_window_open():
                    def seventh_window1_open():
                        def eight_window_open():
                            def next_line_func(list):
                                for i in range(len(list)):
                                    sum = 0
                                    for x in list:
                                        sum += len(x)
                                        i += 1
                                        if sum > 30:
                                            list[i-1] = x + '\n'
                                            print(list)
                                            return item_list_to_str()






                            def item_list_to_str():
                                item_list_str = ''
                                for x in item_list:
                                    item_list_str += x + ', '

                                return item_list_str



                            eight_window = Tk()
                            eight_window.geometry("800x680+700+300")
                            eight_window['bg'] = '#C4C4C4'
                            eight_window.title(" ")
                            inventory_str = inventory_raw.get()
                            inventory_str = inventory_str.lower()
                            item_list = inventory_str.split(',')
                            item_list = [x.strip(' ') for x in item_list]


                                        # придумать как в середину строки  вписать "\n", если она больше 50ти символов



                            window_label_8 = Label(eight_window,
                                                   bg='#C4C4C4',
                                                   text="**Теперь в твоем инвентаре:\n" + next_line_func(item_list) +
                                                        "\n\n\nЕда холодная и ее надо разогреть,"
                                                        "\nиначе ты рискуешь есть холодную еду."
                                                        "\n\nЭто испытание к которому ты сейчас не готов.",
                                                   font=("Arial Bold", 20),
                                                   justify=LEFT,
                                                   padx='60')
                            window_label_8.grid(column=0, row=0,
                                                pady="85")
                            button_ok = Button(eight_window, text="OK",
                                                width="12", height="1", font=("Arial Bold", 18))
                            button_ok.place(x='65', y='630')
                            eight_window.mainloop()

                        def seventh_window1_push_yes():
                            seventh_window1.destroy()
                            eight_window_open()


                        seventh_window1 = Tk()
                        seventh_window1.geometry("600x680+700+300")
                        seventh_window1['bg'] = '#C4C4C4'
                        seventh_window1.title(" ")
                        window_label_7 = Label(seventh_window1,
                                               bg='#C4C4C4',
                                               text="**Это стол. "
                                                    "На нем лежат: "
                                                    "\n\nговяжья нога, луковица, старый"
                                                    "\nщербатый меч, кружка пива, "
                                                    "\nполуголый карлик, "
                                                    "\nсвинина, квашеная \nкапуста, низ собаки"
                                                    "\n\nЧто из этих вещей ты возьмешь в "
                                                    "\nсвой инвентарь? "
                                                    "\n\nВпиши их через запятую", font=("Arial Bold", 20), justify=LEFT,
                                               padx='60')
                        window_label_7.grid(column=0, row=0,
                                            pady="85")
                        inventory_raw = StringVar()
                        entry_seventh_win = Entry(seventh_window1, width=60, textvariable=inventory_raw)
                        entry_seventh_win.place (x='60', y='550')
                        button_yes = Button(seventh_window1, text="ДА",
                                            width="12", height="1", font=("Arial Bold", 18),
                                            command=seventh_window1_push_yes)
                        button_yes.place(x='65', y='630')
                        seventh_window1.mainloop()


                    def seventh_window2_open():
                        def seventh_win2_push_no():
                            seventh_window2.destroy()
                            sixth_window_open()

                        seventh_window2 = Tk()
                        seventh_window2.geometry("600x680+700+300")
                        seventh_window2['bg'] = '#C4C4C4'
                        seventh_window2.title(" ")
                        window_label_8 = Label(seventh_window2,
                                               bg='#C4C4C4',
                                               text="\n**Ты умер от голода в \nжутких мучениях"
                                                    "\n\nВсе твои усилия были \nнапрасны"
                                                    "\n\nСпасибо за игккк",
                                               font=("Arial Bold", 20), justify=LEFT, padx='60')
                        window_label_8.grid(column=0, row=0,
                                            pady="85")
                        button_no = Button(seventh_window2, text="НЕТ",
                                           width="12", height="1", font=("Arial Bold", 18),command=seventh_win2_push_no)
                        button_no.place(x='310', y='630')

                        seventh_window2.mainloop()


                    def sixth_win_push_yes():
                        sixth_window.destroy()
                        seventh_window1_open()


                    def sixth_win_push_no():
                        sixth_window.destroy()
                        seventh_window2_open()


                    sixth_window = Tk()
                    sixth_window.geometry("500x467+700+300")
                    sixth_window['bg'] = '#C4C4C4'
                    sixth_window.title(" ")
                    window_label_6 = Label(sixth_window,
                                           bg='#C4C4C4',
                                           text="**Впереди ты видишь стол с" "\nедой, но не можешь"
                                           "\nрассмотреть,что именно за"
                                           "\nеда на нем "
                                           "\n\nПодойти поближе?",font = ("Arial Bold", 20), justify=LEFT,
                                           padx='60')
                    window_label_6.grid(column=0, row=0,
                                        pady="85")
                    button_yes = Button(sixth_window, text="ДА",
                                        width="12", height="1", font=("Arial Bold", 18), command=sixth_win_push_yes)
                    button_yes.place(x='65', y='360')
                    button_no = Button(sixth_window, text="НЕТ",
                                       width="12", height="1", font=("Arial Bold", 18), command=sixth_win_push_no)
                    button_no.place(x='310', y='360')
                    sixth_window.mainloop()

                def fifth_button_clicked():
                    fifth_window.destroy()
                    sixth_window_open()

                fifth_window = Tk()
                fifth_window.geometry("500x467+700+300")
                fifth_window['bg'] = '#C4C4C4'
                fifth_window.title(" ")
                window_label_5 = Label(fifth_window, bg='#C4C4C4',
                                       text="Чтож, " + name.get()
                                            + "\n\nЯ могу предложить тееб\n"

                                              "отвеать нашей скромной кухни",
                                       font=("Arial Bold", 20),
                                       justify=LEFT, padx='60')
                window_label_5.grid(column=0, row=0, pady="85")
                button_ok_fifth_win = Button(fifth_window,
                                             text="ОК", width="12", height="1", font=("Arial Bold", 18),

                                             command=fifth_button_clicked)
                button_ok_fifth_win.place(x='150', y='370')
                fifth_window.mainloop()

            def fourth_button_clicked():
                fourth_window.destroy()
                fifth_window_open()

            fourth_window = Tk()
            fourth_window.geometry("500x467+700+300")
            fourth_window['bg'] = '#C4C4C4'
            fourth_window.title(" ")
            window_label_4 = Label(fourth_window, bg='#C4C4C4',
                                   text="Достойное имя для\nприключенца!\n \n(моего кота звали так же)",
            font = ("Arial Bold", 20),
                   justify = LEFT, padx = '60')
            window_label_4.grid(column=0, row=0, pady="85")
            button_ok_fourth_win = Button(fourth_window,
                                          text="А?..", width="12", height="1", font=("Arial Bold", 18),

                                          command=fourth_button_clicked)
            button_ok_fourth_win.place(x='150', y='370')
            fourth_window.mainloop()


        def third_window_clicked():
            third_window.destroy()
            fourth_window_open()

        third_window = Tk()
        third_window.geometry("500x467+700+300")
        third_window['bg'] = '#C4C4C4'
        third_window.title(" ")
        window_label_3 = Label(third_window, bg='#C4C4C4',
                               text="Как тебя можно называть?",
                               font=("Arial Bold", 20),
                               justify=LEFT, padx='60')
        window_label_3.grid(column=0, row=0, pady="85")
        name = StringVar()
        entry_third_win = Entry(third_window, width=60,
                                textvariable=name)
        entry_third_win.place(x='60', y='250')
        button_ok_third_win = Button(third_window, text="ДА",
                                     width="12", height="1", font=("Arial Bold", 18),
                                     command=third_window_clicked
                                     )
        button_ok_third_win.place(x='150', y='370')

        third_window.mainloop()

    def second_window_clicked():
        second_window.destroy()
        third_window_open()

    second_window = Tk()
    second_window.geometry("500x467+700+300")
    second_window['bg'] = '#C4C4C4'
    second_window.title(" ")
    button_ok_sec_win = Button(second_window, text="OK",
                               width="12", height="1", font=("Arial Bold", 18),
                               command=second_window_clicked)
    button_ok_sec_win.place(x='150', y='370')
    window_label_2 = Label(second_window, bg='#C4C4C4',
                           text="Отлично! \n"
                                "\nТогда тебе как никому в\nэтом заведении понятно:\n"
                                "\nСытый пуник -- доаольный\nпутник!",
    font = ("Arial Bold", 20), justify = LEFT,
                                         padx = '60')
    window_label_2.grid(column=0, row=0, pady="85")
    second_window.mainloop()


def first_window_clicked():
    first_window.destroy()
    second_window_open()


first_window = Tk()
first_window.geometry("545x410+700+300")
first_window['bg'] = '#C4C4C4'
button_yes = Button(first_window, text="ДА", width="12",
                    height="1", font=("Arial Bold", 18),
                    command=first_window_clicked)
button_yes.place(x='65', y='270')
button_no = Button(first_window, text="НЕТ", width="12",
                   height="1", font=("Arial Bold", 18),
                   command=first_window_clicked)
button_no.place(x='310', y='270')

first_window.title("Приветствую!")
window_label_1 = Label(first_window, bg='#C4C4C4',
                       text="Приветствую пупник! \n" " \nВерно ты устал после долгой \nи опасной дороги?",
font = ("Arial Bold", 20), justify = LEFT,
                                     padx = '60')
window_label_1.grid(column=0, row=0, pady="85")

first_window.mainloop()
