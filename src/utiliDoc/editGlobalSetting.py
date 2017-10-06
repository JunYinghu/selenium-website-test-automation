import time

from CheckRadio import CheckRadio


class editGlobalSetting(CheckRadio):
    def __init__(self, driver, config):
        CheckRadio.__init__(self, driver, config)

    def updateRadio(self):
        time.sleep(10)
        section = 'Board'
        radio_select_n = "location_board_video_id_user_email_n"
        radio_select_y = "location_board_video_id_user_email_y"
        self.selectradio(section, radio_select_n, radio_select_y)
        radio_select_n = "location_board_video_id_admin_email_n"
        radio_select_y = "location_board_video_id_admin_email_y"
        self.selectradio(section, radio_select_n, radio_select_y)
        radio_select_n = 'location_board_video_id_private_msg_n'
        radio_select_y = 'location_board_video_id_private_msg_y'
        self.selectradio(section, radio_select_n, radio_select_y)
        radio_select_n = 'location_board_video_id_hide_online_n'
        radio_select_y = 'location_board_video_id_hide_online_y'
        self.selectradio(section, radio_select_n, radio_select_y)
        radio_select_n = 'location_board_video_id_notify_msg_n'
        radio_select_y = 'location_board_video_id_notify_msg_y'
        self.selectradio(section, radio_select_n, radio_select_y)
        radio_select_n = 'location_board_video_id_pop_win_n'
        radio_select_y = 'location_board_video_id_pop_win_y'
        self.selectradio(section, radio_select_n, radio_select_y)
        radio_select_y = 'location_board_video_id_sum_time_y'
        radio_select_n = 'location_board_video_id_sum_time_n'
        self.selectradio(section, radio_select_n, radio_select_y)
