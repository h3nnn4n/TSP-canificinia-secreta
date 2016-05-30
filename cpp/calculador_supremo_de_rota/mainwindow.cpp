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

    QPixmap pixmap(100,100);
    pixmap.fill(QColor("transparent"));

    QPainter painter(&pixmap);
    painter.setBrush(QBrush(Qt::black));
    painter.drawRect(10, 10, 100, 100);
    ui->mapView->setPixmap(pixmap);
}

void MainWindow::on_actionSair_triggered() {
    QApplication::quit();
}

MainWindow::~MainWindow()
{
    delete ui;
}
