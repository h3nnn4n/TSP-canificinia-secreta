#-------------------------------------------------
#
# Project created by QtCreator 2016-05-26T13:39:47
#
#-------------------------------------------------

INCLUDEPATH += ./include

QMAKE_CXXFLAGS += -std=c++11 -lz

QMAKE_LIBS += -lz -lexpat -lbz2

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = calculador_supremo_de_rota
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp\
        mapLoadder.cpp

HEADERS  += mainwindow.h maploadder.h

FORMS    += mainwindow.ui
