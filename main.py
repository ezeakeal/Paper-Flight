#!/usr/bin/python
import kivy
import interface.main as main

kivy.require('1.5.1')

if __name__ == '__main__':
  main = main.paperApp()
  main.run()
  