import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._ddInsValue = None

    def handle_btn_cerca_iscritti(self, e):
        """Simple function to handle a button-pressed event,
        and consequently print a message on screen"""

        self._view.txt_result.controls.clear()

        if self._ddInsValue is None:
            self._view.create_alert("Per favore selezionare un insegnamento.")
            self._view.update_page()
            return


        studenti = self._model.getIscrittiCorso(self._ddInsValue.codins)
        if not len(studenti):
            self._view.txt_result.controls.append(ft.Text(f"Nessuno studente è iscritto al corso {self._ddInsValue}"))
            return

        self._view.txt_result.controls.append(ft.Text(f"Di seguito gli iscritti al corso {self._ddInsValue}!"))
        self._view.update_page()

        for s in studenti:
            self._view.txt_result.controls.append(ft.Text(s))
            self._view.update_page()

    def handle_btn_cerca_studente(self, e):
        self._view.txt_result.controls.clear()

        if self._view._txtMatricola.value == "":
            self._view.create_alert("Per favore inserire una matricola")
            self._view.update_page()
            return

        matricola = self._view._txtMatricola.value
        studente = self._model.getStudenteFromMatricola(matricola)

        if not len(studente):
            self._view.create_alert(
                f"Non è presente nessuno studente dalla matricola {matricola}"
            )
            self._view.update_page()
            return

        self._view._txtNome.value = f"{studente[0].nome}"
        self._view._txtCognome.value = f"{studente[0].cognome}"
        self._view.update_page()

    def handle_btn_cerca_corsi(self, e):
        self._view.txt_result.controls.clear()

        if self._view._txtMatricola.value == "":
            self._view.create_alert("Per favore inserire una matricola")
            self._view.update_page()
            return

        matricola = self._view._txtMatricola.value
        studente = self._model.getStudenteFromMatricola(matricola)

        if not len(studente):
            self._view.create_alert(
                f"Non è presente nessuno studente dalla matricola {matricola}"
            )
            self._view.update_page()
            return

        corsi = self._model.getCorsiFromMatricola(matricola)
        if not len(corsi):
            self._view.create_alert(
                f"Lo studente{studente[0]} non è iscritto a nessun corso di studi"
            )
            self._view.update_page()
            return

        self._view.txt_result.controls.append(ft.Text(f"Di seguito i corsi a cui lo studente {studente[0].cognome} "
                                                      f"{studente[0].nome} è iscritto:"))
        self._view.update_page()
        for c in corsi:
            self._view.txt_result.controls.append(ft.Text(c))
            self._view.update_page()

    def handle_btn_iscriviti(self, e):
        self._view.txt_result.controls.clear()

        if self._ddInsValue is None:
            self._view.create_alert("Per favore selezionare un insegnamento.")
            self._view.update_page()
            return

        if self._view._txtMatricola.value == "":
            self._view.create_alert("Per favore inserire una matricola")
            self._view.update_page()
            return

        matricola = self._view._txtMatricola.value
        studente = self._model.getStudenteFromMatricola(matricola)

        if not len(studente):
            self._view.create_alert(
                f"Non è presente nessuno studente dalla matricola {matricola}"
            )
            self._view.update_page()
            return

        iscrizione = self._model.getNuovaIscrizione(matricola, self._ddInsValue.codins)

        if iscrizione == 2:
            self._view.create_alert(f"Lo studente {studente[0].cognome} {studente[0].nome} "
                                    f"è già iscritto al corso {self._ddInsValue}")

        if iscrizione == 0:
            self._view.txt_result.controls.append(ft.Text(f"Lo studente {studente[0].cognome} {studente[0].nome} "
                                    f"si è iscritto al corso {self._ddInsValue} ed il database è stato aggiornato"))
            self._view.update_page()

        if iscrizione == 1:
            self._view.txt_result.controls.append(ft.Text(f"Qualcosa è andato storto con l'iscrizione dello "
                                                  f"studente {studente[0].cognome} {studente[0].nome} "
                                                  f"al corso {self._ddInsValue}"))
            self._view.update_page()

    def fill_ddCDS(self):
        for corso in self._model.getAllCorsi():
            self._view._ddCDS.options.append(ft.dropdown.Option(
                key = corso.codins,
                text = corso.__str__(),
                data = corso,
                on_click = self._choiceDDCodins
            ))
            pass

    def _choiceDDCodins(self, e):
        self._ddInsValue = e.control.data
        print(self._ddInsValue)