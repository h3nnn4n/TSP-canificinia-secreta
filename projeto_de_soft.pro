#-------------------------------------------------
#
# Project created by QtCreator 2016-05-11T12:48:01
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = projeto_de_soft
TEMPLATE = app

QMAKE_CXXFLAGS += -L/usr/local/lib -lreadosm -lexpat -lz

SOURCES += main.cpp\
        mainwindow.cpp

HEADERS  += mainwindow.h

FORMS    += mainwindow.ui
