from CheckRadio import CheckRadio


class EditPost(CheckRadio):
    def update(self):
        section = 'editpost'
        radio_select_n = 'location_bbc_code_y'
        radio_select_y = 'location_bbc_code_n'
        self.selectradio(section, radio_select_n, radio_select_y)
        radio_select_n = 'location_smilies_n'
        radio_select_y = 'location_smilies_y'
        self.selectradio(section, radio_select_n, radio_select_y)
        radio_select_n = 'location_signature_n'
        radio_select_y = 'location_signature_y'
        self.selectradio(section, radio_select_n, radio_select_y)
        radio_select_n = 'location_notify_n'
        radio_select_y = 'location_notify_y'
        self.selectradio(section, radio_select_n, radio_select_y)
