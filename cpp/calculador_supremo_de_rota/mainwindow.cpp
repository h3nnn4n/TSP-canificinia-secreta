#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "mapLoadder.h"

#include <QMainWindow>

#include <iostream>
#include <string>

MainWindow::MainWindow(QWidget *parent) : QMainWindow(parent), ui(new Ui::MainWindow) {
    ui->setupUi(this);
    std::string w("map_small.osm");
    ml = new MapLoadder();
    ml->load(w);
    ml->getInfo();
}

void MainWindow::on_actionSair_triggered() {
    QApplication::quit();
}

MainWindow::~MainWindow()
{
    delete ui;
}
