/********************************************************************************
** Form generated from reading UI file 'BlockNote.ui'
**
** Created by: Qt User Interface Compiler version 6.3.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef BLOCKNOTE_H
#define BLOCKNOTE_H

#include <QtCore/QVariant>
#include <QtGui/QIcon>
#include <QtWidgets/QApplication>
#include <QtWidgets/QDialog>
#include <QtWidgets/QFrame>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QPlainTextEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QVBoxLayout>

QT_BEGIN_NAMESPACE

class Ui_Dialog
{
public:
    QVBoxLayout *verticalLayout;
    QPlainTextEdit *pte_blockNote;
    QFrame *frame;
    QVBoxLayout *verticalLayout_2;
    QFrame *frame_2;
    QHBoxLayout *horizontalLayout;
    QPushButton *btn_save;
    QPushButton *btn_clear;

    void setupUi(QDialog *Dialog)
    {
        if (Dialog->objectName().isEmpty())
            Dialog->setObjectName(QString::fromUtf8("Dialog"));
        Dialog->resize(1065, 744);
        Dialog->setMinimumSize(QSize(800, 400));
        QIcon icon;
        icon.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-call-incoming.svg"), QSize(), QIcon::Normal, QIcon::Off);
        Dialog->setWindowIcon(icon);
        Dialog->setStyleSheet(QString::fromUtf8("QPushButton\n"
"{ \n"
"	alternate-background-color: rgb(255, 255, 255);\n"
"	background: rgba(225, 225, 225, 100);\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"	qproperty-iconSize: 32px 32px;\n"
"	border-style: dashed;\n"
" }\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background: rgba(225, 225, 225, 180);\n"
"	border-style: dashed;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	background: rgba(75, 75, 75, 180);\n"
"	border-style: inset;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"QComboBox\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"\n"
"\n"
"QComboBox\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QLine"
                        "Edit:hover{\n"
"	alternate-background-color: rgb(255, 255, 255);\n"
"	background: rgba(225, 225, 225, 100);\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"	qproperty-iconSize: 32px 32px;\n"
"	border-style: dashed;\n"
"    font-size: 24px;\n"
"}\n"
"QLineEdit:pressed{\n"
"	background: rgba(225, 225, 225, 100);\n"
"	border-width: 3px;\n"
"    border-radius: 20px;\n"
"	border-style: line;\n"
"    font-size: 24px;\n"
"}\n"
"QFrame\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"QWidget\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}"));
        verticalLayout = new QVBoxLayout(Dialog);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        pte_blockNote = new QPlainTextEdit(Dialog);
        pte_blockNote->setObjectName(QString::fromUtf8("pte_blockNote"));
        QFont font;
        font.setFamilies({QString::fromUtf8("Cascadia Code PL")});
        font.setPointSize(16);
        pte_blockNote->setFont(font);

        verticalLayout->addWidget(pte_blockNote);

        frame = new QFrame(Dialog);
        frame->setObjectName(QString::fromUtf8("frame"));
        frame->setFrameShape(QFrame::StyledPanel);
        frame->setFrameShadow(QFrame::Raised);
        verticalLayout_2 = new QVBoxLayout(frame);
        verticalLayout_2->setSpacing(0);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        verticalLayout_2->setContentsMargins(0, 0, 0, 0);

        verticalLayout->addWidget(frame);

        frame_2 = new QFrame(Dialog);
        frame_2->setObjectName(QString::fromUtf8("frame_2"));
        frame_2->setFrameShape(QFrame::StyledPanel);
        frame_2->setFrameShadow(QFrame::Raised);
        horizontalLayout = new QHBoxLayout(frame_2);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        btn_save = new QPushButton(frame_2);
        btn_save->setObjectName(QString::fromUtf8("btn_save"));
        QFont font1;
        font1.setPointSize(13);
        btn_save->setFont(font1);
        QIcon icon1;
        icon1.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-cloud-upload.svg"), QSize(), QIcon::Normal, QIcon::Off);
        btn_save->setIcon(icon1);

        horizontalLayout->addWidget(btn_save);

        btn_clear = new QPushButton(frame_2);
        btn_clear->setObjectName(QString::fromUtf8("btn_clear"));
        btn_clear->setFont(font1);
        QIcon icon2;
        icon2.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-trash.svg"), QSize(), QIcon::Normal, QIcon::Off);
        btn_clear->setIcon(icon2);

        horizontalLayout->addWidget(btn_clear);


        verticalLayout->addWidget(frame_2);


        retranslateUi(Dialog);

        QMetaObject::connectSlotsByName(Dialog);
    } // setupUi

    void retranslateUi(QDialog *Dialog)
    {
        Dialog->setWindowTitle(QCoreApplication::translate("Dialog", "Patus Block Note", nullptr));
        btn_save->setText(QCoreApplication::translate("Dialog", "Save and Close", nullptr));
        btn_clear->setText(QCoreApplication::translate("Dialog", "Clear", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Dialog: public Ui_Dialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // BLOCKNOTE_H
