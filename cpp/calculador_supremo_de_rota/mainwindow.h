#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

#include "mapLoadder.h"

namespace Ui {
    class MainWindow;
}

class MainWindow : public QMainWindow {
    Q_OBJECT

    public:
        explicit MainWindow(QWidget *parent = 0);
        ~MainWindow();
        MapLoadder *ml;

    private slots:
        void on_actionSair_triggered();

    private:
        Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H
