#include "mainwindow.h"
#include "ui_mainwindow.h"

#include <iostream>

MainWindow::MainWindow(QWidget *parent) : QMainWindow(parent), ui(new Ui::MainWindow) {
    ui->setupUi(this);
}

void MainWindow::on_actionSair_triggered() {
    std::cout << "Kappa";
    QApplication::quit();
}

MainWindow::~MainWindow()
{
    delete ui;
}
