/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.6.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QMenu>
#include <QtWidgets/QMenuBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QStatusBar>
#include <QtWidgets/QToolBar>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QAction *actionSair;
    QAction *actionAbout;
    QWidget *centralWidget;
    QFrame *frame;
    QGroupBox *groupBox;
    QGroupBox *groupBox_3;
    QCheckBox *chkbox_iluminacao;
    QCheckBox *chkbox_asfaltada;
    QCheckBox *chkbox_maodupla;
    QGroupBox *groupBox_2;
    QWidget *widget;
    QPushButton *btn_limpar;
    QPushButton *btn_calcular;
    QPushButton *btn_salvar;
    QMenuBar *menuBar;
    QMenu *menuArquivo;
    QMenu *menuRelatorios;
    QMenu *menuAjuda;
    QToolBar *mainToolBar;
    QStatusBar *statusBar;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(853, 483);
        actionSair = new QAction(MainWindow);
        actionSair->setObjectName(QStringLiteral("actionSair"));
        actionAbout = new QAction(MainWindow);
        actionAbout->setObjectName(QStringLiteral("actionAbout"));
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        frame = new QFrame(centralWidget);
        frame->setObjectName(QStringLiteral("frame"));
        frame->setGeometry(QRect(2, 0, 850, 421));
        frame->setFrameShape(QFrame::StyledPanel);
        frame->setFrameShadow(QFrame::Raised);
        groupBox = new QGroupBox(frame);
        groupBox->setObjectName(QStringLiteral("groupBox"));
        groupBox->setGeometry(QRect(5, 0, 161, 381));
        groupBox_3 = new QGroupBox(groupBox);
        groupBox_3->setObjectName(QStringLiteral("groupBox_3"));
        groupBox_3->setGeometry(QRect(0, 20, 156, 81));
        chkbox_iluminacao = new QCheckBox(groupBox_3);
        chkbox_iluminacao->setObjectName(QStringLiteral("chkbox_iluminacao"));
        chkbox_iluminacao->setGeometry(QRect(10, 20, 141, 21));
        chkbox_asfaltada = new QCheckBox(groupBox_3);
        chkbox_asfaltada->setObjectName(QStringLiteral("chkbox_asfaltada"));
        chkbox_asfaltada->setGeometry(QRect(10, 40, 90, 21));
        chkbox_maodupla = new QCheckBox(groupBox_3);
        chkbox_maodupla->setObjectName(QStringLiteral("chkbox_maodupla"));
        chkbox_maodupla->setGeometry(QRect(10, 60, 121, 21));
        groupBox_2 = new QGroupBox(frame);
        groupBox_2->setObjectName(QStringLiteral("groupBox_2"));
        groupBox_2->setGeometry(QRect(170, 0, 676, 381));
        widget = new QWidget(groupBox_2);
        widget->setObjectName(QStringLiteral("widget"));
        widget->setGeometry(QRect(0, 20, 671, 361));
        btn_limpar = new QPushButton(frame);
        btn_limpar->setObjectName(QStringLiteral("btn_limpar"));
        btn_limpar->setGeometry(QRect(760, 390, 83, 23));
        btn_calcular = new QPushButton(frame);
        btn_calcular->setObjectName(QStringLiteral("btn_calcular"));
        btn_calcular->setGeometry(QRect(670, 390, 83, 23));
        btn_salvar = new QPushButton(frame);
        btn_salvar->setObjectName(QStringLiteral("btn_salvar"));
        btn_salvar->setGeometry(QRect(580, 390, 83, 23));
        MainWindow->setCentralWidget(centralWidget);
        menuBar = new QMenuBar(MainWindow);
        menuBar->setObjectName(QStringLiteral("menuBar"));
        menuBar->setGeometry(QRect(0, 0, 853, 20));
        menuArquivo = new QMenu(menuBar);
        menuArquivo->setObjectName(QStringLiteral("menuArquivo"));
        menuRelatorios = new QMenu(menuBar);
        menuRelatorios->setObjectName(QStringLiteral("menuRelatorios"));
        menuAjuda = new QMenu(menuBar);
        menuAjuda->setObjectName(QStringLiteral("menuAjuda"));
        MainWindow->setMenuBar(menuBar);
        mainToolBar = new QToolBar(MainWindow);
        mainToolBar->setObjectName(QStringLiteral("mainToolBar"));
        MainWindow->addToolBar(Qt::TopToolBarArea, mainToolBar);
        statusBar = new QStatusBar(MainWindow);
        statusBar->setObjectName(QStringLiteral("statusBar"));
        MainWindow->setStatusBar(statusBar);

        menuBar->addAction(menuArquivo->menuAction());
        menuBar->addAction(menuRelatorios->menuAction());
        menuBar->addAction(menuAjuda->menuAction());
        menuArquivo->addAction(actionSair);
        menuAjuda->addAction(actionAbout);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", 0));
        actionSair->setText(QApplication::translate("MainWindow", "Sair", 0));
        actionAbout->setText(QApplication::translate("MainWindow", "About", 0));
        groupBox->setTitle(QApplication::translate("MainWindow", "Carnificina Secreta", 0));
        groupBox_3->setTitle(QApplication::translate("MainWindow", "Filtros", 0));
        chkbox_iluminacao->setText(QApplication::translate("MainWindow", "Com ilumina\303\247\303\243o", 0));
        chkbox_asfaltada->setText(QApplication::translate("MainWindow", "Asfaltada", 0));
        chkbox_maodupla->setText(QApplication::translate("MainWindow", "M\303\243o Dupla", 0));
        groupBox_2->setTitle(QApplication::translate("MainWindow", "Mapa", 0));
        btn_limpar->setText(QApplication::translate("MainWindow", "Limpar", 0));
        btn_calcular->setText(QApplication::translate("MainWindow", "Calcular", 0));
        btn_salvar->setText(QApplication::translate("MainWindow", "Salvar", 0));
        menuArquivo->setTitle(QApplication::translate("MainWindow", "Arquivo", 0));
        menuRelatorios->setTitle(QApplication::translate("MainWindow", "Relatorios", 0));
        menuAjuda->setTitle(QApplication::translate("MainWindow", "Ajuda", 0));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
