#!/usr/bin/python3
import json
import os
import yaml
import argparse
from os import listdir, system, getenv

class qtheme():

    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("--repo", "-r", help="Choose repository, example : qtile")
        self.parser.add_argument("--theme", "-t", help="Change current system theme")
        self.parser.add_argument("--opacity", "-o", help="Change current alacritty theme opacity")
        self.args = self.parser.parse_args()

    def checkThemeQtile(self):
        for themes in listdir(f"{getenv('HOME')}/.config/qtile/themes/"):
            if themes[:-5] == self.args.theme:
                return True

    def checkThemeAlacritty(self):
        for themes in listdir((f"{getenv('HOME')}/.config/alacritty/themes/")):
            if themes[:-4] == self.args.theme:
                return True


    def saveAlacritty(self):
        if self.checkThemeAlacritty() == True:
            with open(f"{getenv('HOME')}/.config/alacritty/alacritty.yml", "r") as config:
                aconfig = yaml.load(config, Loader=yaml.FullLoader)

                aconfig["import"].clear()
                aconfig["import"].append(f"{getenv('HOME')}/.config/alacritty/themes/{self.args.theme}.yml")

            with open(f"{getenv('HOME')}/.config/alacritty/alacritty.yml", "w") as bconfig:
                yaml.dump(aconfig, bconfig)
            
    def saveQtile(self):
        if self.checkThemeQtile() == True:
            with open(f"{getenv('HOME')}/.config/qtile/themes/{self.args.theme}.json", "r") as settheme:
                tema= json.load(settheme)

            with open(f"{getenv('HOME')}/.config/qtile/theme.json", "r") as config:
                config = json.load(config)
                    
            config["theme"] = self.args.theme 

            with open(f"{getenv('HOME')}/.config/qtile/theme.json", "w") as sconfig:
                json.dump(config, sconfig, indent=4)
            
            os.system("qtile cmd-obj -o cmd -f restart")
    

    def changeAlacrittyOpacity(self):
        with open(f"{getenv('HOME')}/.config/alacritty/themes/{self.args.theme}.yml", "r") as opacity:
            copacity = yaml.load(opacity, Loader=yaml.FullLoader)
        
        copacity["window"]["opacity"] = float(self.args.opacity)

        with open(f"{getenv('HOME')}/.config/alacritty/themes/{self.args.theme}.yml", "w") as opacity:
            yaml.dump(copacity, opacity)


    def saveThemeToConfig(self, theme):
        if self.args.repo == "qtile":
            if self.args.theme:
                self.saveQtile()
        elif self.args.repo == "alacritty":
            if self.args.theme:
                self.saveAlacritty()
                if self.args.opacity:
                    self.changeAlacrittyOpacity()
        else:
            if self.args.theme is not None:
                if not self.args.opacity:
                    self.saveAlacritty()
                    self.saveQtile()
                else:
                    self.changeAlacrittyOpacity()
                    self.saveAlacritty()
                    self.saveQtile()

    def loadTheme(self):

        with open(f"{getenv('HOME')}/.config/qtile/theme.json", "r") as config:
            stema = json.load(config)

        with open(f"{getenv('HOME')}/.config/qtile/themes/{stema['theme']}.json", "r") as ftheme:
            tema = json.load(ftheme)
            return tema

qtile = qtheme()
qtile.saveThemeToConfig(qtile.args.theme)
