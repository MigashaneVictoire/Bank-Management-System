#######################################################################################################
# Expention of for the Baking project... Tihs expention will be completed at a later time of my chosing
#######################################################################################################
# import random
# import pandas as pd
# from os.path import exists as file_exists
# import datetime
# import ThirdPartySyntax as tps
# import smtplib
#
# tps_fix = tps.CustomFix()
# excelFile = "Banking User Info.xlsx"
# file = pd.read_excel(excelFile)
#
#
# class Group():
#     def __init__(self):
#         self._groupID = None
#         self._groupName = ""
#         self.GROUP_SIZE = 0
#
#     def _creatGroup(self):
#         groupID = random.randint(pow(10, 3), pow(10, 5))
#         GROUP_SIZE = Group()._get_group_size()
#         member_info = []
#         for member in range(1, GROUP_SIZE + 1):
#             if member == 1:  ## Group leader
#                 leader = True
#                 email = input("Enter your email address:\n")
#                 Group()._group_emails_coordinates(email)
#                 member_info.append(file[file["Email"] == email])
#                 file.loc[file["Email"]==email]["GroupID"] = groupID
#             else:
#                 email = input(f"Enter member {member} email address: \n")
#                 Group()._group_emails_coordinates(email)
#                 member_info.append(file[file["Email"] == email])
#                 # Group().send_email(email) # can't send email becouse google disabled the passcode singin with less secure apps
#
#         return member_info[0]["GroupID"]
#         # groupName = input("What is the name of your group")
#
#
#     # return the group zipe from user
#     def _get_group_size(self):
#         try:
#             size = int(input("Enter group size including you: \n"))
#             return size if size > 1 and size <=5 else Group()._get_group_size()
#         except ValueError:
#             print("Must enter a number...!")
#             return Group()._get_group_size()
#
#     # collect group member email addresses
#     def _group_emails_coordinates(self, email):
#         return tps_fix._validate_value_in_excel_file(email, True)
#
#     def _groupBalance(self):
#         pass
#
#     def _groupDeposit(self):
#         pass
#
#     def _groupWithdraw(self):
#         pass
