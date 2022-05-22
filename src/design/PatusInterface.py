/********************************************************************************
** Form generated from reading UI file 'PatusInterface.ui'
**
** Created by: Qt User Interface Compiler version 6.3.0
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef PATUSINTERFACE_H
#define PATUSINTERFACE_H

#include <QtCore/QVariant>
#include <QtGui/QIcon>
#include <QtWidgets/QApplication>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QDateEdit>
#include <QtWidgets/QDateTimeEdit>
#include <QtWidgets/QFrame>
#include <QtWidgets/QGridLayout>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLCDNumber>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QRadioButton>
#include <QtWidgets/QScrollArea>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QStackedWidget>
#include <QtWidgets/QTabWidget>
#include <QtWidgets/QTableWidget>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_PatusMainWindow
{
public:
    QWidget *w_background;
    QVBoxLayout *verticalLayout;
    QFrame *f_main;
    QHBoxLayout *horizontalLayout;
    QFrame *f_sideBar;
    QVBoxLayout *verticalLayout_2;
    QPushButton *btn_logInOut;
    QPushButton *btn_tables;
    QPushButton *btn_cashRegister;
    QPushButton *btn_reservation;
    QPushButton *btn_waste;
    QPushButton *btn_databaseOverview;
    QPushButton *btn_productReceipt;
    QPushButton *btn_database;
    QPushButton *btn_workerStatus;
    QPushButton *btn_statistic;
    QPushButton *btn_exit;
    QFrame *f_body;
    QVBoxLayout *verticalLayout_3;
    QFrame *f_header;
    QHBoxLayout *horizontalLayout_3;
    QFrame *f_btn_sideBar;
    QHBoxLayout *horizontalLayout_4;
    QPushButton *btn_sideBar;
    QFrame *f_headerInfo;
    QGridLayout *gridLayout_2;
    QLabel *l_busyTables;
    QLabel *l_monthSells;
    QLabel *l_freeTables;
    QLabel *l_daySells;
    QFrame *f_btn_fullScreen;
    QHBoxLayout *horizontalLayout_5;
    QPushButton *btn_blockNote;
    QPushButton *btn_notification;
    QPushButton *btn_setting;
    QPushButton *btn_fullScreen;
    QFrame *f_content;
    QVBoxLayout *verticalLayout_16;
    QStackedWidget *sw_content;
    QWidget *page_standBy;
    QGridLayout *gridLayout;
    QSpacerItem *hs_standByR;
    QSpacerItem *vs_standByT;
    QFrame *f_standBy;
    QVBoxLayout *verticalLayout_4;
    QLabel *l_date;
    QLabel *l_time;
    QLabel *l_welcomeMsg;
    QSpacerItem *hs_standByL;
    QSpacerItem *vs_standByB;
    QWidget *page_login;
    QGridLayout *gridLayout_3;
    QFrame *f_longin;
    QVBoxLayout *verticalLayout_5;
    QPushButton *btn_biometric;
    QLineEdit *le_username;
    QLineEdit *le_password;
    QPushButton *btn_loginConfirm;
    QSpacerItem *hs_loginR;
    QSpacerItem *hs_loginL;
    QWidget *page_tables;
    QGridLayout *gridLayout_4;
    QWidget *page_cashRegister;
    QGridLayout *gridLayout_5;
    QFrame *f_orderDashboard;
    QVBoxLayout *verticalLayout_7;
    QFrame *frame_5;
    QHBoxLayout *horizontalLayout_31;
    QLabel *l_cashRegisterTicketNumberTitle;
    QLabel *l_cashRegisterTicketNumber;
    QFrame *frame_9;
    QHBoxLayout *horizontalLayout_32;
    QLabel *l_cashRegisterTableNumberTitle;
    QLabel *l_cashRegisterTableNumber;
    QPushButton *btn_cashRegisterChangeTable;
    QFrame *f_orderPlace;
    QHBoxLayout *horizontalLayout_56;
    QRadioButton *rb_takeAway;
    QRadioButton *rb_onTable;
    QFrame *f_cashCommand;
    QVBoxLayout *verticalLayout_9;
    QFrame *f_orderNav;
    QHBoxLayout *horizontalLayout_6;
    QFrame *f_ticket;
    QVBoxLayout *verticalLayout_8;
    QPushButton *btn_cashRegisterDeleteCurrent;
    QPushButton *btn_cashRegisterClear;
    QPushButton *btn_cashRegisterResume;
    QPushButton *btn_cashRegisterHold;
    QFrame *f_totalInfo;
    QGridLayout *gridLayout_8;
    QLabel *l_taxDa;
    QLabel *l_totalTtc;
    QLabel *l_da;
    QLCDNumber *lcdN_totalHtt;
    QLCDNumber *lcdN_tax;
    QLabel *l_totalHtt;
    QLCDNumber *lcdN_totalTtc;
    QLabel *l_tax;
    QLabel *l_TtcDa;
    QFrame *f_cashButtons;
    QVBoxLayout *verticalLayout_15;
    QPushButton *btn_cashRegisterReduce;
    QPushButton *btn_cashRegisterTicketKitchen;
    QPushButton *btn_cashRegisterTicket;
    QPushButton *btn_cashRegisterPay;
    QFrame *f_orderWorker;
    QHBoxLayout *horizontalLayout_63;
    QLabel *l_orderWorker;
    QComboBox *cb_orderWorker;
    QFrame *f_orderCustomer;
    QHBoxLayout *horizontalLayout_7;
    QLabel *l_orderCustomer;
    QComboBox *cb_orderCustomer;
    QTableWidget *tw_orderList;
    QGroupBox *groupBox_2;
    QVBoxLayout *verticalLayout_50;
    QTextEdit *le_cashRegisterComment;
    QFrame *f_foodMenu;
    QVBoxLayout *verticalLayout_6;
    QTabWidget *tw_foodMenu;
    QWidget *tab_salade;
    QGridLayout *gridLayout_12;
    QScrollArea *sa_salade;
    QWidget *w_salade;
    QGridLayout *gridLayout_13;
    QFrame *frame_7;
    QVBoxLayout *verticalLayout_57;
    QLabel *label_15;
    QLabel *label_16;
    QFrame *frame_15;
    QHBoxLayout *horizontalLayout_34;
    QPushButton *pushButton_38;
    QPushButton *pushButton_39;
    QFrame *frame_16;
    QVBoxLayout *verticalLayout_58;
    QLabel *label_17;
    QLabel *label_18;
    QFrame *frame_17;
    QHBoxLayout *horizontalLayout_35;
    QPushButton *pushButton_40;
    QPushButton *pushButton_41;
    QFrame *frame_39;
    QVBoxLayout *verticalLayout_91;
    QLabel *label_32;
    QLabel *label_33;
    QFrame *frame_42;
    QHBoxLayout *horizontalLayout_68;
    QPushButton *pushButton_56;
    QPushButton *pushButton_57;
    QWidget *tab_meal;
    QVBoxLayout *verticalLayout_10;
    QScrollArea *sa_meal;
    QWidget *w_meal;
    QGridLayout *gridLayout_6;
    QFrame *frame_18;
    QVBoxLayout *verticalLayout_59;
    QLabel *label_19;
    QLabel *label_20;
    QFrame *frame_19;
    QHBoxLayout *horizontalLayout_36;
    QPushButton *pushButton_42;
    QPushButton *pushButton_43;
    QFrame *frame_20;
    QVBoxLayout *verticalLayout_60;
    QLabel *label_21;
    QLabel *label_22;
    QFrame *frame_21;
    QHBoxLayout *horizontalLayout_37;
    QPushButton *pushButton_44;
    QPushButton *pushButton_45;
    QFrame *frame_41;
    QVBoxLayout *verticalLayout_90;
    QLabel *label_29;
    QLabel *label_31;
    QFrame *frame_44;
    QHBoxLayout *horizontalLayout_65;
    QPushButton *pushButton_54;
    QPushButton *pushButton_55;
    QWidget *tab_pizza;
    QVBoxLayout *verticalLayout_11;
    QScrollArea *sa_pizza;
    QWidget *w_pizza;
    QGridLayout *gridLayout_7;
    QFrame *frame;
    QVBoxLayout *verticalLayout_43;
    QLabel *label;
    QLabel *label_5;
    QFrame *frame_2;
    QHBoxLayout *horizontalLayout_25;
    QPushButton *pushButton_4;
    QPushButton *pushButton_14;
    QFrame *frame_3;
    QVBoxLayout *verticalLayout_44;
    QLabel *label_2;
    QLabel *label_6;
    QFrame *frame_4;
    QHBoxLayout *horizontalLayout_26;
    QPushButton *pushButton_15;
    QPushButton *pushButton_16;
    QFrame *frame_48;
    QVBoxLayout *verticalLayout_92;
    QLabel *label_3;
    QLabel *label_7;
    QFrame *frame_49;
    QHBoxLayout *horizontalLayout_69;
    QPushButton *pushButton_17;
    QPushButton *pushButton_18;
    QWidget *tab_coldDrink;
    QVBoxLayout *verticalLayout_12;
    QScrollArea *sa_coldDrink;
    QWidget *w_coldDrink;
    QGridLayout *gridLayout_11;
    QFrame *frame_24;
    QVBoxLayout *verticalLayout_62;
    QLabel *label_25;
    QLabel *label_26;
    QFrame *frame_25;
    QHBoxLayout *horizontalLayout_39;
    QPushButton *pushButton_48;
    QPushButton *pushButton_49;
    QFrame *frame_22;
    QVBoxLayout *verticalLayout_61;
    QLabel *label_23;
    QLabel *label_24;
    QFrame *frame_23;
    QHBoxLayout *horizontalLayout_38;
    QPushButton *pushButton_46;
    QPushButton *pushButton_47;
    QFrame *frame_50;
    QVBoxLayout *verticalLayout_95;
    QLabel *label_34;
    QLabel *label_41;
    QFrame *frame_51;
    QHBoxLayout *horizontalLayout_72;
    QPushButton *pushButton_64;
    QPushButton *pushButton_65;
    QWidget *tab_hotDrink;
    QVBoxLayout *verticalLayout_13;
    QScrollArea *sa_hotDrink;
    QWidget *w_hotDrink;
    QGridLayout *gridLayout_16;
    QFrame *frame_28;
    QVBoxLayout *verticalLayout_67;
    QLabel *label_35;
    QLabel *label_36;
    QFrame *frame_30;
    QHBoxLayout *horizontalLayout_44;
    QPushButton *pushButton_58;
    QPushButton *pushButton_59;
    QFrame *frame_26;
    QVBoxLayout *verticalLayout_63;
    QLabel *label_27;
    QLabel *label_28;
    QFrame *frame_27;
    QHBoxLayout *horizontalLayout_40;
    QPushButton *pushButton_50;
    QPushButton *pushButton_51;
    QFrame *frame_52;
    QVBoxLayout *verticalLayout_96;
    QLabel *label_44;
    QLabel *label_45;
    QFrame *frame_53;
    QHBoxLayout *horizontalLayout_73;
    QPushButton *pushButton_70;
    QPushButton *pushButton_71;
    QWidget *tab_dessert;
    QVBoxLayout *verticalLayout_14;
    QScrollArea *sa_dessert;
    QWidget *w_dessert;
    QGridLayout *gridLayout_17;
    QFrame *frame_36;
    QVBoxLayout *verticalLayout_69;
    QLabel *label_39;
    QLabel *label_40;
    QFrame *frame_37;
    QHBoxLayout *horizontalLayout_46;
    QPushButton *pushButton_62;
    QPushButton *pushButton_63;
    QFrame *frame_34;
    QVBoxLayout *verticalLayout_68;
    QLabel *label_37;
    QLabel *label_38;
    QComboBox *comboBox;
    QFrame *frame_35;
    QHBoxLayout *horizontalLayout_45;
    QPushButton *pushButton_60;
    QPushButton *pushButton_61;
    QFrame *frame_54;
    QVBoxLayout *verticalLayout_97;
    QLabel *label_46;
    QLabel *label_47;
    QFrame *frame_55;
    QHBoxLayout *horizontalLayout_74;
    QPushButton *pushButton_72;
    QPushButton *pushButton_73;
    QWidget *page_reservation;
    QHBoxLayout *horizontalLayout_51;
    QFrame *f_reservationInputs;
    QVBoxLayout *verticalLayout_72;
    QGroupBox *gb_reservation;
    QVBoxLayout *verticalLayout_73;
    QLineEdit *le_reservationName;
    QLineEdit *le_reservationPhone;
    QLineEdit *le_reservationNbPerson;
    QDateTimeEdit *dte_reservation;
    QTableWidget *tw_reservationTable;
    QFrame *f_expenseDbBtn_5;
    QHBoxLayout *horizontalLayout_50;
    QPushButton *btn_reservationAdd;
    QPushButton *btn_reservationEdit;
    QPushButton *btn_reservationDelete;
    QPushButton *btn_reservationClear;
    QFrame *f_reservationDb;
    QVBoxLayout *verticalLayout_71;
    QFrame *frame_10;
    QHBoxLayout *horizontalLayout_52;
    QComboBox *cb_reservationSearchType;
    QLineEdit *le_reservationSearch;
    QPushButton *btn_reservationSearch;
    QFrame *frame_11;
    QHBoxLayout *horizontalLayout_53;
    QCheckBox *cb_reservationDate;
    QDateEdit *de_reservationSearchDate;
    QTableWidget *tw_reservation;
    QWidget *page_waste;
    QHBoxLayout *horizontalLayout_24;
    QFrame *w_wasteCustom;
    QVBoxLayout *verticalLayout_29;
    QGroupBox *groupBox_4;
    QVBoxLayout *verticalLayout_74;
    QComboBox *cb_wasteStockWorkerId;
    QLineEdit *le_wasteStockQuantity;
    QTableWidget *tw_wasteStock;
    QFrame *frame_29;
    QHBoxLayout *horizontalLayout_30;
    QPushButton *btn_wasteStockClear;
    QPushButton *btn_wasteStockSave;
    QGroupBox *groupBox_3;
    QVBoxLayout *verticalLayout_54;
    QComboBox *cb_wasteCustomWorkerId;
    QLineEdit *le_wasteCustomName;
    QComboBox *cb_wasteCustomCategory;
    QLineEdit *le_wasteCustomQuantity;
    QLineEdit *le_wasteCustomPrice;
    QFrame *frame1;
    QHBoxLayout *horizontalLayout_29;
    QPushButton *btn_wasteCustomClear;
    QPushButton *btn_wasteCustomSave;
    QFrame *w_wasteStock;
    QVBoxLayout *verticalLayout_36;
    QTableWidget *tw_waste;
    QWidget *page_overview;
    QHBoxLayout *horizontalLayout_33;
    QFrame *frame_12;
    QVBoxLayout *verticalLayout_49;
    QLabel *l_stock;
    QFrame *frame_38;
    QHBoxLayout *horizontalLayout_57;
    QRadioButton *rb_stockIngredients;
    QRadioButton *rb_stockOthers;
    QTableWidget *tw_stock;
    QWidget *page_productReceipt;
    QGridLayout *gridLayout_14;
    QFrame *frame_6;
    QVBoxLayout *verticalLayout_48;
    QLabel *l_productReceiptSelection;
    QFrame *frame_14;
    QGridLayout *gridLayout_22;
    QLabel *l_ingredient_2;
    QComboBox *cb_productReceiptMenuItem;
    QFrame *frame_8;
    QGridLayout *gridLayout_15;
    QPushButton *btn_productReceiptAdd;
    QComboBox *cb_productReceiptIngredientName;
    QPushButton *btn_productReceiptRemove;
    QLineEdit *le_productReceiptIngredientQuantity;
    QPushButton *btn_productReceiptEdit;
    QLabel *l_ingredient;
    QPushButton *btn_productReceiptClear;
    QTableWidget *tw_productReceiptIngredientList;
    QFrame *frame_31;
    QGridLayout *gridLayout_23;
    QLabel *l_ingredient_7;
    QLabel *l_ingredient_5;
    QLabel *l_ingredient_8;
    QLabel *l_productReceiptQuantity;
    QLabel *l_productReceiptPrice;
    QLabel *l_productReceiptEstimatedProductionPrice;
    QWidget *page_database;
    QGridLayout *gridLayout_9;
    QTabWidget *tw_database;
    QWidget *tab_menu;
    QHBoxLayout *horizontalLayout_8;
    QFrame *f_menuItemInputs;
    QVBoxLayout *verticalLayout_18;
    QGroupBox *gb_menuItem;
    QVBoxLayout *verticalLayout_19;
    QFrame *f_menuItemPic;
    QHBoxLayout *horizontalLayout_17;
    QLabel *l_menuItemPicture;
    QFrame *f_finishProductPictureSetting;
    QVBoxLayout *verticalLayout_41;
    QPushButton *btn_menuItemPicture;
    QPushButton *btn_menuItemPictureClear;
    QLineEdit *le_menuItemName;
    QComboBox *cb_menuItemCategory;
    QComboBox *cb_menuItemCategoryCustom;
    QLineEdit *le_menuItemUnit;
    QLineEdit *le_menuItemUnitQuantity;
    QLineEdit *le_menuItemPrice;
    QFrame *f_menuItemDbBtn;
    QHBoxLayout *horizontalLayout_16;
    QPushButton *btn_menuItemAdd;
    QPushButton *btn_menuItemEdit;
    QPushButton *btn_menuItemDelete;
    QPushButton *btn_menuItemClear;
    QFrame *f_menuItemDb;
    QVBoxLayout *verticalLayout_17;
    QTableWidget *tw_menuItem;
    QWidget *tab;
    QGridLayout *gridLayout_19;
    QFrame *f_menuCategoryCustomDb;
    QVBoxLayout *verticalLayout_77;
    QTableWidget *tw_menuCategoryCustom;
    QFrame *f_menuCategoryCustom;
    QVBoxLayout *verticalLayout_75;
    QGroupBox *gb_menuCategoryCustom;
    QVBoxLayout *verticalLayout_76;
    QLineEdit *le_menuCategoryCustomName;
    QComboBox *cb_menuCategoryCustomPrinting;
    QFrame *f_menuCategoryCustomDbBtn;
    QHBoxLayout *horizontalLayout_54;
    QPushButton *btn_menuCategoryCustomAdd;
    QPushButton *btn_menuCategoryCustomEdit;
    QPushButton *btn_menuCategoryCustomDelete;
    QPushButton *btn_menuCategoryCustomClear;
    QWidget *tab_supplement;
    QHBoxLayout *horizontalLayout_49;
    QFrame *f_supplementInputs;
    QVBoxLayout *verticalLayout_66;
    QGroupBox *gb_supplement;
    QVBoxLayout *verticalLayout_70;
    QLineEdit *le_supplementName;
    QComboBox *cb_supplementProduct;
    QLineEdit *le_supplementQuantity;
    QLineEdit *le_supplementPrice;
    QFrame *f_expenseDbBtn_4;
    QHBoxLayout *horizontalLayout_48;
    QPushButton *btn_supplementAdd;
    QPushButton *btn_supplementEdit;
    QPushButton *btn_supplementDelete;
    QPushButton *btn_supplementClear;
    QFrame *f_supplementDb;
    QVBoxLayout *verticalLayout_65;
    QTableWidget *tw_supplement;
    QWidget *tab_expense;
    QHBoxLayout *horizontalLayout_9;
    QFrame *f_expenseInputs;
    QVBoxLayout *verticalLayout_20;
    QGroupBox *gb_expense;
    QVBoxLayout *verticalLayout_21;
    QLineEdit *le_expenseName;
    QComboBox *cb_expenseCategory;
    QLineEdit *le_expenseUnit;
    QLineEdit *le_expenseQuantity;
    QLineEdit *le_expensePrice;
    QComboBox *cb_expenseSupplier;
    QCheckBox *cb_expensePayed;
    QFrame *f_expenseDbBtn;
    QHBoxLayout *horizontalLayout_18;
    QPushButton *btn_expenseAdd;
    QPushButton *btn_expenseEdit;
    QPushButton *btn_expenseDelete;
    QPushButton *btn_expenseClear;
    QFrame *f_expenseDb;
    QVBoxLayout *verticalLayout_22;
    QTableWidget *tw_expense;
    QWidget *tab_expenseCategory;
    QHBoxLayout *horizontalLayout_42;
    QFrame *f_expenseCategoryInputs;
    QVBoxLayout *verticalLayout_52;
    QGroupBox *gb_expenseCategory;
    QVBoxLayout *verticalLayout_53;
    QLineEdit *le_expenseCategoryName;
    QCheckBox *cb_expenseCategorySaveToStock;
    QCheckBox *cb_expenseCategoryIsIngredient;
    QFrame *f_expenseCategoryDbBtn;
    QHBoxLayout *horizontalLayout_41;
    QPushButton *btn_expenseCategoryAdd;
    QPushButton *btn_expenseCategoryEdit;
    QPushButton *btn_expenseCategoryDelete;
    QPushButton *btn_expenseCategoryClear;
    QFrame *f_expenseCategoryDb;
    QVBoxLayout *verticalLayout_51;
    QTableWidget *tw_expenseCategory;
    QWidget *tab_supplier;
    QHBoxLayout *horizontalLayout_47;
    QFrame *f_supplierInputs;
    QVBoxLayout *verticalLayout_56;
    QGroupBox *gb_supplier;
    QVBoxLayout *verticalLayout_64;
    QLineEdit *le_supplierName;
    QLineEdit *le_supplierPhone;
    QLineEdit *le_supplierAddress;
    QLineEdit *le_supplierMail;
    QFrame *f_expenseDbBtn_3;
    QHBoxLayout *horizontalLayout_43;
    QPushButton *btn_supplierAdd;
    QPushButton *btn_supplierEdit;
    QPushButton *btn_supplierDelete;
    QPushButton *btn_supplierClear;
    QFrame *f_supplierDb;
    QVBoxLayout *verticalLayout_55;
    QTableWidget *tw_supplier;
    QWidget *tab_customer;
    QHBoxLayout *horizontalLayout_10;
    QFrame *f_customerInput;
    QVBoxLayout *verticalLayout_40;
    QGroupBox *gb_customer;
    QVBoxLayout *verticalLayout_24;
    QFrame *f_customerPic;
    QHBoxLayout *horizontalLayout_27;
    QLabel *l_customerPicture;
    QFrame *f_customerSetting;
    QVBoxLayout *verticalLayout_45;
    QPushButton *btn_customerPicture;
    QPushButton *btn_customerPictureClear;
    QLineEdit *le_customerName;
    QLineEdit *le_customerPhone;
    QLineEdit *le_customerAddress;
    QLineEdit *le_customerScore;
    QFrame *f_customerDbBtn;
    QHBoxLayout *horizontalLayout_19;
    QPushButton *btn_customerAdd;
    QPushButton *btn_customerEdit;
    QPushButton *btn_customerDelete;
    QPushButton *btn_customerClear;
    QFrame *f_cutosmerDb;
    QVBoxLayout *verticalLayout_23;
    QTableWidget *tw_customer;
    QWidget *tab_worker;
    QHBoxLayout *horizontalLayout_11;
    QFrame *f_workerInput;
    QVBoxLayout *verticalLayout_35;
    QGroupBox *gb_worker;
    QVBoxLayout *verticalLayout_25;
    QFrame *f_workerPic;
    QHBoxLayout *horizontalLayout_28;
    QLabel *l_workerPicture;
    QFrame *f_workerPictureSetting;
    QVBoxLayout *verticalLayout_46;
    QPushButton *btn_workerPicture;
    QPushButton *btn_workerPictureClear;
    QLineEdit *le_workerName;
    QComboBox *cb_workerCategory;
    QLineEdit *le_workerUsername;
    QLineEdit *le_workerPassword;
    QLineEdit *le_workerPhone;
    QLineEdit *le_workerAddress;
    QLineEdit *le_workerSalary;
    QLineEdit *le_workerScore;
    QFrame *frame_33;
    QHBoxLayout *horizontalLayout_58;
    QLineEdit *le_workerCv;
    QPushButton *btn_workerAddCv;
    QPushButton *btn_workerOpenCv;
    QPushButton *btn_workerClearCv;
    QFrame *f_workerDbBtn;
    QHBoxLayout *horizontalLayout_20;
    QPushButton *btn_workerAdd;
    QPushButton *btn_workerEdit;
    QPushButton *btn_workerDelete;
    QPushButton *btn_workerClear;
    QFrame *f_workerDb;
    QVBoxLayout *verticalLayout_30;
    QTableWidget *tw_worker;
    QWidget *tab_category;
    QHBoxLayout *horizontalLayout_14;
    QFrame *f_categoryInput;
    QVBoxLayout *verticalLayout_37;
    QGroupBox *gb_category;
    QVBoxLayout *verticalLayout_28;
    QLineEdit *le_categoryName;
    QFrame *frame_32;
    QGridLayout *gridLayout_24;
    QCheckBox *cb_categoryLevelCashier;
    QCheckBox *cb_categoryLevelWaste;
    QCheckBox *cb_categoryLevelTables;
    QCheckBox *cb_categoryLevelStock;
    QCheckBox *cb_categoryLevelReservation;
    QCheckBox *cb_categoryLevelReceipt;
    QCheckBox *cb_categoryLevelDb;
    QCheckBox *cb_categoryLevelPhone;
    QCheckBox *cb_categoryLevelStat;
    QFrame *f_categoryDbBtn;
    QHBoxLayout *horizontalLayout_23;
    QPushButton *btn_categoryAdd;
    QPushButton *btn_categoryEdit;
    QPushButton *btn_categoryDelete;
    QPushButton *btn_categoryClear;
    QFrame *f_categoryDb;
    QVBoxLayout *verticalLayout_33;
    QTableWidget *tw_category;
    QWidget *tab_sell;
    QHBoxLayout *horizontalLayout_12;
    QFrame *f_sellInput;
    QVBoxLayout *verticalLayout_39;
    QGroupBox *gb_sell;
    QVBoxLayout *verticalLayout_26;
    QComboBox *cb_sellIdWorker;
    QComboBox *cb_sellIdCustomer;
    QDateTimeEdit *dte_sellDate;
    QLineEdit *le_sellTotal;
    QLineEdit *le_sellNbCovers;
    QFrame *f_sellDbBtn;
    QHBoxLayout *horizontalLayout_21;
    QPushButton *btn_sellAdd;
    QPushButton *btn_sellEdit;
    QPushButton *btn_sellDelete;
    QPushButton *btn_sellClear;
    QPushButton *btn_sellShow;
    QPushButton *btn_sellLoad;
    QFrame *f_sellDb;
    QVBoxLayout *verticalLayout_31;
    QTableWidget *tw_sell;
    QWidget *tab_table;
    QHBoxLayout *horizontalLayout_13;
    QFrame *f_tableInput;
    QVBoxLayout *verticalLayout_38;
    QGroupBox *gb_expense_6;
    QVBoxLayout *verticalLayout_27;
    QLineEdit *le_tableName;
    QLineEdit *le_tableId;
    QLineEdit *le_tableSeats;
    QLineEdit *le_tableComment;
    QFrame *f_tableDbBtn;
    QHBoxLayout *horizontalLayout_22;
    QPushButton *btn_tableAdd;
    QPushButton *btn_tableEdit;
    QPushButton *btn_tableDelete;
    QPushButton *btn_tableClear;
    QFrame *f_tableDb;
    QVBoxLayout *verticalLayout_32;
    QTableWidget *tw_table;
    QWidget *tab_pointer;
    QHBoxLayout *horizontalLayout_15;
    QFrame *f_pointerDb;
    QVBoxLayout *verticalLayout_34;
    QGroupBox *groupBox;
    QVBoxLayout *verticalLayout_47;
    QTableWidget *tw_pointer;
    QWidget *tab_stock;
    QHBoxLayout *horizontalLayout_60;
    QFrame *f_tableInput_2;
    QVBoxLayout *verticalLayout_42;
    QGroupBox *gb_stock;
    QVBoxLayout *verticalLayout_79;
    QLineEdit *le_stockProductName;
    QComboBox *cb_stockCategory;
    QLineEdit *le_stockUnit;
    QLineEdit *le_stockQuantity;
    QCheckBox *cb_stockIsIngredient;
    QFrame *f_tableDbBtn_2;
    QHBoxLayout *horizontalLayout_59;
    QPushButton *btn_stockAdd;
    QPushButton *btn_stockEdit;
    QPushButton *btn_stockDelete;
    QPushButton *btn_stockClear;
    QFrame *f_stockDb;
    QVBoxLayout *verticalLayout_80;
    QTableWidget *tw_stockDb;
    QWidget *tab_uploader;
    QHBoxLayout *horizontalLayout_62;
    QFrame *f_tableInput_3;
    QVBoxLayout *verticalLayout_82;
    QGroupBox *gb_doccuments;
    QVBoxLayout *verticalLayout_83;
    QLineEdit *le_docName;
    QDateTimeEdit *dte_docDate;
    QLineEdit *le_docComment;
    QFrame *frame_40;
    QHBoxLayout *horizontalLayout_64;
    QLineEdit *le_docPath;
    QPushButton *btn_docAddFile;
    QPushButton *btn_docOpenFile;
    QPushButton *btn_docClearFile;
    QFrame *f_tableDbBtn_3;
    QHBoxLayout *horizontalLayout_61;
    QPushButton *btn_docAdd;
    QPushButton *btn_docEdit;
    QPushButton *btn_docDelete;
    QPushButton *btn_docClear;
    QFrame *f_stockDb_2;
    QVBoxLayout *verticalLayout_81;
    QTableWidget *tw_documentDb;
    QWidget *tab_tableOwnership;
    QHBoxLayout *horizontalLayout_67;
    QFrame *f_tableOwnershipInput;
    QVBoxLayout *verticalLayout_88;
    QGroupBox *gb_tableOwnership;
    QVBoxLayout *verticalLayout_89;
    QComboBox *cb_tableOwnershipTableId;
    QComboBox *cb_tableOwnershipWorkerId;
    QFrame *f_tableDbBtn_4;
    QHBoxLayout *horizontalLayout_66;
    QPushButton *btn_tableOwnershipAdd;
    QPushButton *btn_tableOwnershipEdit;
    QPushButton *btn_tableOwnershipDelete;
    QPushButton *btn_tableOwnershipClear;
    QFrame *f_tableOwnershipDb;
    QVBoxLayout *verticalLayout_87;
    QTableWidget *tw_tableOwnershipDb;
    QWidget *page_workerStatus;
    QGridLayout *gridLayout_20;
    QScrollArea *sa_workerStatus;
    QWidget *w_workerStats;
    QGridLayout *gridLayout_21;
    QFrame *frame_13;
    QVBoxLayout *verticalLayout_78;
    QLabel *label_30;
    QTextEdit *textEdit;
    QFrame *frame_291;
    QHBoxLayout *horizontalLayout_55;
    QPushButton *pushButton_52;
    QPushButton *pushButton_53;
    QFrame *frame_43;
    QVBoxLayout *verticalLayout_93;
    QLabel *label_42;
    QTextEdit *textEdit_2;
    QFrame *frame_45;
    QHBoxLayout *horizontalLayout_70;
    QPushButton *pushButton_66;
    QPushButton *pushButton_67;
    QFrame *frame_46;
    QVBoxLayout *verticalLayout_94;
    QLabel *label_43;
    QTextEdit *textEdit_3;
    QFrame *frame_47;
    QHBoxLayout *horizontalLayout_71;
    QPushButton *pushButton_68;
    QPushButton *pushButton_69;
    QWidget *page_stats;
    QGridLayout *gridLayout_18;
    QFrame *f_footer;
    QHBoxLayout *horizontalLayout_2;
    QLabel *l_version;
    QLabel *l_serverStatus;
    QLabel *l_creator;
    QPushButton *btn_logs;
    QFrame *f_notification;
    QVBoxLayout *verticalLayout_84;
    QScrollArea *scrollArea;
    QWidget *scrollAreaWidgetContents;
    QVBoxLayout *verticalLayout_85;
    QWidget *w_notification;
    QVBoxLayout *verticalLayout_86;
    QPushButton *btn_notification_clear;

    void setupUi(QMainWindow *PatusMainWindow)
    {
        if (PatusMainWindow->objectName().isEmpty())
            PatusMainWindow->setObjectName(QString::fromUtf8("PatusMainWindow"));
        PatusMainWindow->resize(1100, 816);
        PatusMainWindow->setMinimumSize(QSize(1100, 800));
        QIcon icon;
        icon.addFile(QString::fromUtf8(":/Simple icons/patus_logo.svg"), QSize(), QIcon::Normal, QIcon::Off);
        PatusMainWindow->setWindowIcon(icon);
        PatusMainWindow->setStyleSheet(QString::fromUtf8("#page_tables{\n"
"	border-image: url(resource/Restaurant_plan/plan.png) 0 0 0 0 stretch stretch;\n"
"}\n"
"\n"
"QPushButton\n"
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
""
                        "	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
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
        w_background = new QWidget(PatusMainWindow);
        w_background->setObjectName(QString::fromUtf8("w_background"));
        verticalLayout = new QVBoxLayout(w_background);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        verticalLayout->setContentsMargins(0, 0, 0, 0);
        f_main = new QFrame(w_background);
        f_main->setObjectName(QString::fromUtf8("f_main"));
        f_main->setTabletTracking(false);
        f_main->setStyleSheet(QString::fromUtf8(""));
        f_main->setFrameShape(QFrame::StyledPanel);
        f_main->setFrameShadow(QFrame::Raised);
        horizontalLayout = new QHBoxLayout(f_main);
        horizontalLayout->setSpacing(0);
        horizontalLayout->setObjectName(QString::fromUtf8("horizontalLayout"));
        horizontalLayout->setContentsMargins(0, 0, 0, 0);
        f_sideBar = new QFrame(f_main);
        f_sideBar->setObjectName(QString::fromUtf8("f_sideBar"));
        f_sideBar->setMinimumSize(QSize(100, 0));
        f_sideBar->setMaximumSize(QSize(100, 16777215));
        f_sideBar->setTabletTracking(false);
        f_sideBar->setStyleSheet(QString::fromUtf8("QFrame\n"
"{\n"
"	background-color: rgb(190, 190, 190)\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	\n"
"	alternate-background-color: rgb(255, 255, 255);\n"
"	background: rgba(225, 225, 225, 100);\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"	qproperty-iconSize: 50px 50px;\n"
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
"	background: rgba(225, 225, 225, 255);\n"
"	border-style: inset;\n"
"}"));
        f_sideBar->setFrameShape(QFrame::StyledPanel);
        f_sideBar->setFrameShadow(QFrame::Raised);
        verticalLayout_2 = new QVBoxLayout(f_sideBar);
        verticalLayout_2->setSpacing(20);
        verticalLayout_2->setObjectName(QString::fromUtf8("verticalLayout_2"));
        verticalLayout_2->setContentsMargins(9, 9, 9, 9);
        btn_logInOut = new QPushButton(f_sideBar);
        btn_logInOut->setObjectName(QString::fromUtf8("btn_logInOut"));
        QSizePolicy sizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(btn_logInOut->sizePolicy().hasHeightForWidth());
        btn_logInOut->setSizePolicy(sizePolicy);
        btn_logInOut->setTabletTracking(false);
        QIcon icon1;
        icon1.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-user.svg"), QSize(), QIcon::Normal, QIcon::Off);
        btn_logInOut->setIcon(icon1);
        btn_logInOut->setIconSize(QSize(50, 50));

        verticalLayout_2->addWidget(btn_logInOut);

        btn_tables = new QPushButton(f_sideBar);
        btn_tables->setObjectName(QString::fromUtf8("btn_tables"));
        btn_tables->setEnabled(false);
        sizePolicy.setHeightForWidth(btn_tables->sizePolicy().hasHeightForWidth());
        btn_tables->setSizePolicy(sizePolicy);
        btn_tables->setTabletTracking(false);
        QIcon icon2;
        icon2.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-terrace.svg"), QSize(), QIcon::Normal, QIcon::Off);
        btn_tables->setIcon(icon2);
        btn_tables->setIconSize(QSize(50, 50));

        verticalLayout_2->addWidget(btn_tables);

        btn_cashRegister = new QPushButton(f_sideBar);
        btn_cashRegister->setObjectName(QString::fromUtf8("btn_cashRegister"));
        btn_cashRegister->setEnabled(false);
        sizePolicy.setHeightForWidth(btn_cashRegister->sizePolicy().hasHeightForWidth());
        btn_cashRegister->setSizePolicy(sizePolicy);
        btn_cashRegister->setTabletTracking(false);
        QIcon icon3;
        icon3.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-shop.svg"), QSize(), QIcon::Normal, QIcon::Off);
        btn_cashRegister->setIcon(icon3);
        btn_cashRegister->setIconSize(QSize(50, 50));

        verticalLayout_2->addWidget(btn_cashRegister);

        btn_reservation = new QPushButton(f_sideBar);
        btn_reservation->setObjectName(QString::fromUtf8("btn_reservation"));
        btn_reservation->setEnabled(false);
        sizePolicy.setHeightForWidth(btn_reservation->sizePolicy().hasHeightForWidth());
        btn_reservation->setSizePolicy(sizePolicy);
        btn_reservation->setTabletTracking(false);
        QIcon icon4;
        icon4.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-phone-call.svg"), QSize(), QIcon::Normal, QIcon::Off);
        btn_reservation->setIcon(icon4);
        btn_reservation->setIconSize(QSize(50, 50));

        verticalLayout_2->addWidget(btn_reservation);

        btn_waste = new QPushButton(f_sideBar);
        btn_waste->setObjectName(QString::fromUtf8("btn_waste"));
        btn_waste->setEnabled(false);
        sizePolicy.setHeightForWidth(btn_waste->sizePolicy().hasHeightForWidth());
        btn_waste->setSizePolicy(sizePolicy);
        btn_waste->setTabletTracking(false);
        QIcon icon5;
        icon5.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-sad.svg"), QSize(), QIcon::Normal, QIcon::Off);
        btn_waste->setIcon(icon5);
        btn_waste->setIconSize(QSize(50, 50));

        verticalLayout_2->addWidget(btn_waste);

        btn_databaseOverview = new QPushButton(f_sideBar);
        btn_databaseOverview->setObjectName(QString::fromUtf8("btn_databaseOverview"));
        btn_databaseOverview->setEnabled(false);
        sizePolicy.setHeightForWidth(btn_databaseOverview->sizePolicy().hasHeightForWidth());
        btn_databaseOverview->setSizePolicy(sizePolicy);
        btn_databaseOverview->setTabletTracking(false);
        QIcon icon6;
        icon6.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-home.svg"), QSize(), QIcon::Normal, QIcon::Off);
        btn_databaseOverview->setIcon(icon6);
        btn_databaseOverview->setIconSize(QSize(50, 50));

        verticalLayout_2->addWidget(btn_databaseOverview);

        btn_productReceipt = new QPushButton(f_sideBar);
        btn_productReceipt->setObjectName(QString::fromUtf8("btn_productReceipt"));
        btn_productReceipt->setEnabled(false);
        sizePolicy.setHeightForWidth(btn_productReceipt->sizePolicy().hasHeightForWidth());
        btn_productReceipt->setSizePolicy(sizePolicy);
        btn_productReceipt->setTabletTracking(false);
        QIcon icon7;
        icon7.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-list.svg"), QSize(), QIcon::Normal, QIcon::Off);
        btn_productReceipt->setIcon(icon7);
        btn_productReceipt->setIconSize(QSize(50, 50));

        verticalLayout_2->addWidget(btn_productReceipt);

        btn_database = new QPushButton(f_sideBar);
        btn_database->setObjectName(QString::fromUtf8("btn_database"));
        btn_database->setEnabled(false);
        sizePolicy.setHeightForWidth(btn_database->sizePolicy().hasHeightForWidth());
        btn_database->setSizePolicy(sizePolicy);
        btn_database->setTabletTracking(false);
        QIcon icon8;
        icon8.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-database.svg"), QSize(), QIcon::Normal, QIcon::Off);
        btn_database->setIcon(icon8);
        btn_database->setIconSize(QSize(50, 50));

        verticalLayout_2->addWidget(btn_database);

        btn_workerStatus = new QPushButton(f_sideBar);
        btn_workerStatus->setObjectName(QString::fromUtf8("btn_workerStatus"));
        btn_workerStatus->setEnabled(false);
        sizePolicy.setHeightForWidth(btn_workerStatus->sizePolicy().hasHeightForWidth());
        btn_workerStatus->setSizePolicy(sizePolicy);
        btn_workerStatus->setTabletTracking(false);
        QIcon icon9;
        icon9.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-data-transfer.svg"), QSize(), QIcon::Normal, QIcon::Off);
        btn_workerStatus->setIcon(icon9);
        btn_workerStatus->setIconSize(QSize(50, 50));

        verticalLayout_2->addWidget(btn_workerStatus);

        btn_statistic = new QPushButton(f_sideBar);
        btn_statistic->setObjectName(QString::fromUtf8("btn_statistic"));
        btn_statistic->setEnabled(false);
        sizePolicy.setHeightForWidth(btn_statistic->sizePolicy().hasHeightForWidth());
        btn_statistic->setSizePolicy(sizePolicy);
        btn_statistic->setTabletTracking(false);
        QIcon icon10;
        icon10.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-stats.svg"), QSize(), QIcon::Normal, QIcon::Off);
        btn_statistic->setIcon(icon10);
        btn_statistic->setIconSize(QSize(50, 50));

        verticalLayout_2->addWidget(btn_statistic);

        btn_exit = new QPushButton(f_sideBar);
        btn_exit->setObjectName(QString::fromUtf8("btn_exit"));
        btn_exit->setEnabled(false);
        sizePolicy.setHeightForWidth(btn_exit->sizePolicy().hasHeightForWidth());
        btn_exit->setSizePolicy(sizePolicy);
        btn_exit->setTabletTracking(false);
        QIcon icon11;
        icon11.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-sign-out.svg"), QSize(), QIcon::Normal, QIcon::Off);
        btn_exit->setIcon(icon11);
        btn_exit->setIconSize(QSize(50, 50));

        verticalLayout_2->addWidget(btn_exit);


        horizontalLayout->addWidget(f_sideBar);

        f_body = new QFrame(f_main);
        f_body->setObjectName(QString::fromUtf8("f_body"));
        f_body->setTabletTracking(false);
        f_body->setStyleSheet(QString::fromUtf8("#f_body{\n"
"background-color: rgba(208, 208, 208, 150);\n"
"}"));
        f_body->setFrameShape(QFrame::StyledPanel);
        f_body->setFrameShadow(QFrame::Raised);
        verticalLayout_3 = new QVBoxLayout(f_body);
        verticalLayout_3->setSpacing(1);
        verticalLayout_3->setObjectName(QString::fromUtf8("verticalLayout_3"));
        verticalLayout_3->setContentsMargins(2, 1, 1, 1);
        f_header = new QFrame(f_body);
        f_header->setObjectName(QString::fromUtf8("f_header"));
        QSizePolicy sizePolicy1(QSizePolicy::Preferred, QSizePolicy::Maximum);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(f_header->sizePolicy().hasHeightForWidth());
        f_header->setSizePolicy(sizePolicy1);
        f_header->setMinimumSize(QSize(0, 50));
        f_header->setTabletTracking(false);
        f_header->setStyleSheet(QString::fromUtf8("#f_header{\n"
"	background-color: qlineargradient(spread:reflect, x1:0.460227, y1:1, x2:1, y2:1, stop:0 rgba(218, 218, 218, 255), stop:0.625 rgba(135, 135, 135, 255));\n"
"}"));
        f_header->setFrameShape(QFrame::StyledPanel);
        f_header->setFrameShadow(QFrame::Raised);
        horizontalLayout_3 = new QHBoxLayout(f_header);
        horizontalLayout_3->setSpacing(0);
        horizontalLayout_3->setObjectName(QString::fromUtf8("horizontalLayout_3"));
        horizontalLayout_3->setContentsMargins(0, 0, 0, 0);
        f_btn_sideBar = new QFrame(f_header);
        f_btn_sideBar->setObjectName(QString::fromUtf8("f_btn_sideBar"));
        QSizePolicy sizePolicy2(QSizePolicy::Minimum, QSizePolicy::Preferred);
        sizePolicy2.setHorizontalStretch(0);
        sizePolicy2.setVerticalStretch(0);
        sizePolicy2.setHeightForWidth(f_btn_sideBar->sizePolicy().hasHeightForWidth());
        f_btn_sideBar->setSizePolicy(sizePolicy2);
        f_btn_sideBar->setMinimumSize(QSize(50, 50));
        f_btn_sideBar->setMaximumSize(QSize(50, 50));
        f_btn_sideBar->setTabletTracking(false);
        f_btn_sideBar->setStyleSheet(QString::fromUtf8("QFrame\n"
"{\n"
"	background-color:  rgba(223, 223, 223, 200);\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	background: rgba(225, 225, 225, 20);\n"
"	border-width: 2px;\n"
"    border-radius: 2px;\n"
"	qproperty-iconSize: 32px 32px;\n"
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
"	background: rgba(225, 225, 225, 255);\n"
"	border-style: inset;\n"
"}"));
        f_btn_sideBar->setFrameShape(QFrame::StyledPanel);
        f_btn_sideBar->setFrameShadow(QFrame::Raised);
        horizontalLayout_4 = new QHBoxLayout(f_btn_sideBar);
        horizontalLayout_4->setSpacing(0);
        horizontalLayout_4->setObjectName(QString::fromUtf8("horizontalLayout_4"));
        horizontalLayout_4->setContentsMargins(0, 0, 0, 0);
        btn_sideBar = new QPushButton(f_btn_sideBar);
        btn_sideBar->setObjectName(QString::fromUtf8("btn_sideBar"));
        QSizePolicy sizePolicy3(QSizePolicy::MinimumExpanding, QSizePolicy::MinimumExpanding);
        sizePolicy3.setHorizontalStretch(0);
        sizePolicy3.setVerticalStretch(0);
        sizePolicy3.setHeightForWidth(btn_sideBar->sizePolicy().hasHeightForWidth());
        btn_sideBar->setSizePolicy(sizePolicy3);
        btn_sideBar->setTabletTracking(false);
        QIcon icon12;
        icon12.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-align-left.svg"), QSize(), QIcon::Normal, QIcon::Off);
        btn_sideBar->setIcon(icon12);

        horizontalLayout_4->addWidget(btn_sideBar);


        horizontalLayout_3->addWidget(f_btn_sideBar);

        f_headerInfo = new QFrame(f_header);
        f_headerInfo->setObjectName(QString::fromUtf8("f_headerInfo"));
        sizePolicy1.setHeightForWidth(f_headerInfo->sizePolicy().hasHeightForWidth());
        f_headerInfo->setSizePolicy(sizePolicy1);
        f_headerInfo->setTabletTracking(false);
        f_headerInfo->setStyleSheet(QString::fromUtf8("*\n"
"{\n"
"	color: rgb(33, 33, 33);\n"
"	font: 12pt \"Times New Roman\";\n"
"    border-radius: 30px;\n"
"	padding: 2px;\n"
"}\n"
"QLabel\n"
"{\n"
"	background: transparent\n"
"}"));
        f_headerInfo->setFrameShape(QFrame::StyledPanel);
        f_headerInfo->setFrameShadow(QFrame::Raised);
        gridLayout_2 = new QGridLayout(f_headerInfo);
        gridLayout_2->setSpacing(0);
        gridLayout_2->setObjectName(QString::fromUtf8("gridLayout_2"));
        gridLayout_2->setContentsMargins(0, 0, 0, 0);
        l_busyTables = new QLabel(f_headerInfo);
        l_busyTables->setObjectName(QString::fromUtf8("l_busyTables"));
        sizePolicy1.setHeightForWidth(l_busyTables->sizePolicy().hasHeightForWidth());
        l_busyTables->setSizePolicy(sizePolicy1);
        l_busyTables->setTabletTracking(false);
        l_busyTables->setAlignment(Qt::AlignCenter);

        gridLayout_2->addWidget(l_busyTables, 2, 0, 1, 1);

        l_monthSells = new QLabel(f_headerInfo);
        l_monthSells->setObjectName(QString::fromUtf8("l_monthSells"));
        sizePolicy1.setHeightForWidth(l_monthSells->sizePolicy().hasHeightForWidth());
        l_monthSells->setSizePolicy(sizePolicy1);
        l_monthSells->setTabletTracking(false);
        l_monthSells->setAlignment(Qt::AlignCenter);

        gridLayout_2->addWidget(l_monthSells, 2, 1, 1, 1);

        l_freeTables = new QLabel(f_headerInfo);
        l_freeTables->setObjectName(QString::fromUtf8("l_freeTables"));
        sizePolicy1.setHeightForWidth(l_freeTables->sizePolicy().hasHeightForWidth());
        l_freeTables->setSizePolicy(sizePolicy1);
        l_freeTables->setTabletTracking(false);
        l_freeTables->setAlignment(Qt::AlignCenter);

        gridLayout_2->addWidget(l_freeTables, 0, 0, 1, 1);

        l_daySells = new QLabel(f_headerInfo);
        l_daySells->setObjectName(QString::fromUtf8("l_daySells"));
        sizePolicy1.setHeightForWidth(l_daySells->sizePolicy().hasHeightForWidth());
        l_daySells->setSizePolicy(sizePolicy1);
        l_daySells->setTabletTracking(false);
        l_daySells->setAlignment(Qt::AlignCenter);

        gridLayout_2->addWidget(l_daySells, 0, 1, 1, 1);


        horizontalLayout_3->addWidget(f_headerInfo);

        f_btn_fullScreen = new QFrame(f_header);
        f_btn_fullScreen->setObjectName(QString::fromUtf8("f_btn_fullScreen"));
        sizePolicy2.setHeightForWidth(f_btn_fullScreen->sizePolicy().hasHeightForWidth());
        f_btn_fullScreen->setSizePolicy(sizePolicy2);
        f_btn_fullScreen->setMinimumSize(QSize(150, 50));
        f_btn_fullScreen->setMaximumSize(QSize(200, 50));
        f_btn_fullScreen->setTabletTracking(false);
        f_btn_fullScreen->setStyleSheet(QString::fromUtf8("QFrame\n"
"{\n"
"	background-color:  rgba(223, 223, 223, 200);\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	background: rgba(225, 225, 225, 20);\n"
"	border-width: 2px;\n"
"    border-radius: 2px;\n"
"	qproperty-iconSize: 32px 32px;\n"
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
"	background: rgba(225, 225, 225, 255);\n"
"	border-style: inset;\n"
"}"));
        f_btn_fullScreen->setFrameShape(QFrame::StyledPanel);
        f_btn_fullScreen->setFrameShadow(QFrame::Raised);
        horizontalLayout_5 = new QHBoxLayout(f_btn_fullScreen);
        horizontalLayout_5->setSpacing(0);
        horizontalLayout_5->setObjectName(QString::fromUtf8("horizontalLayout_5"));
        horizontalLayout_5->setContentsMargins(0, 0, 0, 0);
        btn_blockNote = new QPushButton(f_btn_fullScreen);
        btn_blockNote->setObjectName(QString::fromUtf8("btn_blockNote"));
        btn_blockNote->setEnabled(true);
        sizePolicy3.setHeightForWidth(btn_blockNote->sizePolicy().hasHeightForWidth());
        btn_blockNote->setSizePolicy(sizePolicy3);
        btn_blockNote->setTabletTracking(false);
        QIcon icon13;
        icon13.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-call-incoming.svg"), QSize(), QIcon::Normal, QIcon::Off);
        btn_blockNote->setIcon(icon13);

        horizontalLayout_5->addWidget(btn_blockNote);

        btn_notification = new QPushButton(f_btn_fullScreen);
        btn_notification->setObjectName(QString::fromUtf8("btn_notification"));
        btn_notification->setEnabled(false);
        sizePolicy3.setHeightForWidth(btn_notification->sizePolicy().hasHeightForWidth());
        btn_notification->setSizePolicy(sizePolicy3);
        btn_notification->setTabletTracking(false);
        QIcon icon14;
        icon14.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-envelope-marker.svg"), QSize(), QIcon::Normal, QIcon::Off);
        btn_notification->setIcon(icon14);

        horizontalLayout_5->addWidget(btn_notification);

        btn_setting = new QPushButton(f_btn_fullScreen);
        btn_setting->setObjectName(QString::fromUtf8("btn_setting"));
        sizePolicy3.setHeightForWidth(btn_setting->sizePolicy().hasHeightForWidth());
        btn_setting->setSizePolicy(sizePolicy3);
        btn_setting->setTabletTracking(false);
        QIcon icon15;
        icon15.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-settings.svg"), QSize(), QIcon::Normal, QIcon::Off);
        btn_setting->setIcon(icon15);

        horizontalLayout_5->addWidget(btn_setting);

        btn_fullScreen = new QPushButton(f_btn_fullScreen);
        btn_fullScreen->setObjectName(QString::fromUtf8("btn_fullScreen"));
        sizePolicy3.setHeightForWidth(btn_fullScreen->sizePolicy().hasHeightForWidth());
        btn_fullScreen->setSizePolicy(sizePolicy3);
        btn_fullScreen->setTabletTracking(false);
        QIcon icon16;
        icon16.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-compress.svg"), QSize(), QIcon::Normal, QIcon::Off);
        btn_fullScreen->setIcon(icon16);

        horizontalLayout_5->addWidget(btn_fullScreen);


        horizontalLayout_3->addWidget(f_btn_fullScreen);


        verticalLayout_3->addWidget(f_header);

        f_content = new QFrame(f_body);
        f_content->setObjectName(QString::fromUtf8("f_content"));
        f_content->setTabletTracking(false);
        f_content->setFrameShape(QFrame::StyledPanel);
        f_content->setFrameShadow(QFrame::Raised);
        verticalLayout_16 = new QVBoxLayout(f_content);
        verticalLayout_16->setSpacing(0);
        verticalLayout_16->setObjectName(QString::fromUtf8("verticalLayout_16"));
        verticalLayout_16->setContentsMargins(0, 0, 0, 0);
        sw_content = new QStackedWidget(f_content);
        sw_content->setObjectName(QString::fromUtf8("sw_content"));
        sw_content->setTabletTracking(false);
        sw_content->setStyleSheet(QString::fromUtf8(""));
        sw_content->setFrameShape(QFrame::Box);
        page_standBy = new QWidget();
        page_standBy->setObjectName(QString::fromUtf8("page_standBy"));
        gridLayout = new QGridLayout(page_standBy);
        gridLayout->setObjectName(QString::fromUtf8("gridLayout"));
        hs_standByR = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(hs_standByR, 1, 2, 1, 1);

        vs_standByT = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(vs_standByT, 0, 1, 1, 1);

        f_standBy = new QFrame(page_standBy);
        f_standBy->setObjectName(QString::fromUtf8("f_standBy"));
        sizePolicy3.setHeightForWidth(f_standBy->sizePolicy().hasHeightForWidth());
        f_standBy->setSizePolicy(sizePolicy3);
        f_standBy->setMinimumSize(QSize(350, 200));
        f_standBy->setMaximumSize(QSize(800, 600));
        QFont font;
        font.setFamilies({QString::fromUtf8("Times New Roman")});
        font.setPointSize(28);
        font.setBold(false);
        font.setItalic(false);
        f_standBy->setFont(font);
        f_standBy->setStyleSheet(QString::fromUtf8("*\n"
"{\n"
"	background-color: rgba(149, 149, 149, 200);\n"
"	color: rgb(230, 230, 230);\n"
"	font: 28pt \"Times New Roman\";\n"
"    border-radius: 30px;\n"
"	padding: 2px;\n"
"}\n"
"QLabel\n"
"{\n"
"	background: transparent\n"
"}"));
        f_standBy->setFrameShape(QFrame::StyledPanel);
        f_standBy->setFrameShadow(QFrame::Raised);
        f_standBy->setLineWidth(1);
        verticalLayout_4 = new QVBoxLayout(f_standBy);
        verticalLayout_4->setSpacing(0);
        verticalLayout_4->setObjectName(QString::fromUtf8("verticalLayout_4"));
        verticalLayout_4->setContentsMargins(0, -1, 0, 0);
        l_date = new QLabel(f_standBy);
        l_date->setObjectName(QString::fromUtf8("l_date"));
        l_date->setAlignment(Qt::AlignCenter);

        verticalLayout_4->addWidget(l_date);

        l_time = new QLabel(f_standBy);
        l_time->setObjectName(QString::fromUtf8("l_time"));
        l_time->setAlignment(Qt::AlignCenter);

        verticalLayout_4->addWidget(l_time);

        l_welcomeMsg = new QLabel(f_standBy);
        l_welcomeMsg->setObjectName(QString::fromUtf8("l_welcomeMsg"));
        l_welcomeMsg->setAlignment(Qt::AlignCenter);

        verticalLayout_4->addWidget(l_welcomeMsg);


        gridLayout->addWidget(f_standBy, 1, 1, 1, 1);

        hs_standByL = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout->addItem(hs_standByL, 1, 0, 1, 1);

        vs_standByB = new QSpacerItem(20, 40, QSizePolicy::Minimum, QSizePolicy::Expanding);

        gridLayout->addItem(vs_standByB, 2, 1, 1, 1);

        sw_content->addWidget(page_standBy);
        page_login = new QWidget();
        page_login->setObjectName(QString::fromUtf8("page_login"));
        gridLayout_3 = new QGridLayout(page_login);
        gridLayout_3->setObjectName(QString::fromUtf8("gridLayout_3"));
        f_longin = new QFrame(page_login);
        f_longin->setObjectName(QString::fromUtf8("f_longin"));
        sizePolicy.setHeightForWidth(f_longin->sizePolicy().hasHeightForWidth());
        f_longin->setSizePolicy(sizePolicy);
        f_longin->setMinimumSize(QSize(100, 200));
        f_longin->setMaximumSize(QSize(400, 16777215));
        f_longin->setStyleSheet(QString::fromUtf8("*\n"
"{\n"
"	background: rgb(0, 0, 0);\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"	color: white;\n"
"	padding: 2px;\n"
"}\n"
"\n"
"QFrame\n"
"{\n"
"	background:rgba(72, 72, 72, 200);\n"
"	border-width: 6px;\n"
"    border-radius: 30px;\n"
"}\n"
"\n"
"\n"
"#btn_biometric:hover\n"
"{\n"
"	background: rgba(225, 225, 225, 120);\n"
"}\n"
"\n"
"#btn_biometric:pressed\n"
"{\n"
"	background: rgba(225, 225, 225, 150);\n"
"}\n"
"\n"
"\n"
"QPushButton\n"
"{ \n"
"	alternate-background-color: rgb(0, 0, 0);\n"
"	background: rgba(225, 225, 225, 100);\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"	qproperty-iconSize: 100px 100px;\n"
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
"	background: rgba(225, 225, 225, 255);\n"
"	border-style: inset;\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(207, 207, 207);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072\n"
"}\n"
""));
        f_longin->setFrameShape(QFrame::StyledPanel);
        f_longin->setFrameShadow(QFrame::Raised);
        verticalLayout_5 = new QVBoxLayout(f_longin);
        verticalLayout_5->setObjectName(QString::fromUtf8("verticalLayout_5"));
        btn_biometric = new QPushButton(f_longin);
        btn_biometric->setObjectName(QString::fromUtf8("btn_biometric"));
        QSizePolicy sizePolicy4(QSizePolicy::Minimum, QSizePolicy::Minimum);
        sizePolicy4.setHorizontalStretch(0);
        sizePolicy4.setVerticalStretch(0);
        sizePolicy4.setHeightForWidth(btn_biometric->sizePolicy().hasHeightForWidth());
        btn_biometric->setSizePolicy(sizePolicy4);
        btn_biometric->setMinimumSize(QSize(200, 200));
        btn_biometric->setMaximumSize(QSize(400, 400));
        btn_biometric->setLayoutDirection(Qt::LeftToRight);
        QIcon icon17;
        icon17.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-fingerprint.svg"), QSize(), QIcon::Normal, QIcon::Off);
        btn_biometric->setIcon(icon17);

        verticalLayout_5->addWidget(btn_biometric);

        le_username = new QLineEdit(f_longin);
        le_username->setObjectName(QString::fromUtf8("le_username"));
        le_username->setMaxLength(20);
        le_username->setClearButtonEnabled(true);

        verticalLayout_5->addWidget(le_username);

        le_password = new QLineEdit(f_longin);
        le_password->setObjectName(QString::fromUtf8("le_password"));
        le_password->setMaxLength(15);
        le_password->setEchoMode(QLineEdit::Password);
        le_password->setClearButtonEnabled(true);

        verticalLayout_5->addWidget(le_password);

        btn_loginConfirm = new QPushButton(f_longin);
        btn_loginConfirm->setObjectName(QString::fromUtf8("btn_loginConfirm"));
        QSizePolicy sizePolicy5(QSizePolicy::Preferred, QSizePolicy::Fixed);
        sizePolicy5.setHorizontalStretch(0);
        sizePolicy5.setVerticalStretch(0);
        sizePolicy5.setHeightForWidth(btn_loginConfirm->sizePolicy().hasHeightForWidth());
        btn_loginConfirm->setSizePolicy(sizePolicy5);
        btn_loginConfirm->setMinimumSize(QSize(0, 50));
        btn_loginConfirm->setMaximumSize(QSize(16777215, 50));
        btn_loginConfirm->setCheckable(true);

        verticalLayout_5->addWidget(btn_loginConfirm);


        gridLayout_3->addWidget(f_longin, 0, 1, 1, 1);

        hs_loginR = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_3->addItem(hs_loginR, 0, 2, 1, 1);

        hs_loginL = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        gridLayout_3->addItem(hs_loginL, 0, 0, 1, 1);

        sw_content->addWidget(page_login);
        page_tables = new QWidget();
        page_tables->setObjectName(QString::fromUtf8("page_tables"));
        page_tables->setStyleSheet(QString::fromUtf8("*\n"
"{\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"	padding: 2px;\n"
"}\n"
"QPushButton\n"
"{ \n"
"	alternate-background-color: rgb(255, 255, 255);\n"
"	background: rgba(225, 225, 225, 255);\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"	qproperty-iconSize: 32px 32px;\n"
"	border-style: dashed;\n"
" }\n"
"\n"
"QPushButton:hover\n"
"{\n"
"	background: rgba(225, 225, 225, 100);\n"
"	border-style: dashed;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"	background: rgba(75, 75, 75, 180);\n"
"	border-style: inset;\n"
"}"));
        gridLayout_4 = new QGridLayout(page_tables);
        gridLayout_4->setObjectName(QString::fromUtf8("gridLayout_4"));
        sw_content->addWidget(page_tables);
        page_cashRegister = new QWidget();
        page_cashRegister->setObjectName(QString::fromUtf8("page_cashRegister"));
        page_cashRegister->setStyleSheet(QString::fromUtf8("QPushButton\n"
"{ \n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"	padding: 2px;\n"
"	alternate-background-color: rgb(255, 255, 255);\n"
"	background: rgba(225, 225, 225, 100);\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"	qproperty-iconSize: 50px 50px;\n"
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
"	background: rgba(225, 225, 225, 255);\n"
"	border-style: inset;\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"	alignment: \"center\"\n"
"}"));
        gridLayout_5 = new QGridLayout(page_cashRegister);
        gridLayout_5->setObjectName(QString::fromUtf8("gridLayout_5"));
        f_orderDashboard = new QFrame(page_cashRegister);
        f_orderDashboard->setObjectName(QString::fromUtf8("f_orderDashboard"));
        QSizePolicy sizePolicy6(QSizePolicy::Maximum, QSizePolicy::Preferred);
        sizePolicy6.setHorizontalStretch(0);
        sizePolicy6.setVerticalStretch(0);
        sizePolicy6.setHeightForWidth(f_orderDashboard->sizePolicy().hasHeightForWidth());
        f_orderDashboard->setSizePolicy(sizePolicy6);
        f_orderDashboard->setMinimumSize(QSize(200, 0));
        f_orderDashboard->setMaximumSize(QSize(600, 16777215));
        f_orderDashboard->setTabletTracking(false);
        f_orderDashboard->setStyleSheet(QString::fromUtf8("\n"
"QPushButton\n"
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
"\n"
"\n"
"QComboBox\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}"));
        f_orderDashboard->setFrameShape(QFrame::StyledPanel);
        f_orderDashboard->setFrameShadow(QFrame::Raised);
        verticalLayout_7 = new QVBoxLayout(f_orderDashboard);
        verticalLayout_7->setSpacing(2);
        verticalLayout_7->setObjectName(QString::fromUtf8("verticalLayout_7"));
        verticalLayout_7->setContentsMargins(0, 0, 0, 0);
        frame_5 = new QFrame(f_orderDashboard);
        frame_5->setObjectName(QString::fromUtf8("frame_5"));
        frame_5->setTabletTracking(false);
        frame_5->setFrameShape(QFrame::StyledPanel);
        frame_5->setFrameShadow(QFrame::Sunken);
        horizontalLayout_31 = new QHBoxLayout(frame_5);
        horizontalLayout_31->setObjectName(QString::fromUtf8("horizontalLayout_31"));
        l_cashRegisterTicketNumberTitle = new QLabel(frame_5);
        l_cashRegisterTicketNumberTitle->setObjectName(QString::fromUtf8("l_cashRegisterTicketNumberTitle"));
        l_cashRegisterTicketNumberTitle->setTabletTracking(false);

        horizontalLayout_31->addWidget(l_cashRegisterTicketNumberTitle);

        l_cashRegisterTicketNumber = new QLabel(frame_5);
        l_cashRegisterTicketNumber->setObjectName(QString::fromUtf8("l_cashRegisterTicketNumber"));
        l_cashRegisterTicketNumber->setTabletTracking(false);
        l_cashRegisterTicketNumber->setAlignment(Qt::AlignCenter);

        horizontalLayout_31->addWidget(l_cashRegisterTicketNumber);


        verticalLayout_7->addWidget(frame_5);

        frame_9 = new QFrame(f_orderDashboard);
        frame_9->setObjectName(QString::fromUtf8("frame_9"));
        frame_9->setTabletTracking(false);
        frame_9->setFrameShape(QFrame::StyledPanel);
        frame_9->setFrameShadow(QFrame::Sunken);
        horizontalLayout_32 = new QHBoxLayout(frame_9);
        horizontalLayout_32->setObjectName(QString::fromUtf8("horizontalLayout_32"));
        l_cashRegisterTableNumberTitle = new QLabel(frame_9);
        l_cashRegisterTableNumberTitle->setObjectName(QString::fromUtf8("l_cashRegisterTableNumberTitle"));
        l_cashRegisterTableNumberTitle->setTabletTracking(false);

        horizontalLayout_32->addWidget(l_cashRegisterTableNumberTitle);

        l_cashRegisterTableNumber = new QLabel(frame_9);
        l_cashRegisterTableNumber->setObjectName(QString::fromUtf8("l_cashRegisterTableNumber"));
        l_cashRegisterTableNumber->setTabletTracking(false);
        l_cashRegisterTableNumber->setAlignment(Qt::AlignCenter);

        horizontalLayout_32->addWidget(l_cashRegisterTableNumber);

        btn_cashRegisterChangeTable = new QPushButton(frame_9);
        btn_cashRegisterChangeTable->setObjectName(QString::fromUtf8("btn_cashRegisterChangeTable"));
        sizePolicy4.setHeightForWidth(btn_cashRegisterChangeTable->sizePolicy().hasHeightForWidth());
        btn_cashRegisterChangeTable->setSizePolicy(sizePolicy4);
        btn_cashRegisterChangeTable->setMaximumSize(QSize(50, 16777215));
        btn_cashRegisterChangeTable->setTabletTracking(false);
        QIcon icon18;
        icon18.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-apps-sort.svg"), QSize(), QIcon::Normal, QIcon::Off);
        btn_cashRegisterChangeTable->setIcon(icon18);
        btn_cashRegisterChangeTable->setIconSize(QSize(32, 32));

        horizontalLayout_32->addWidget(btn_cashRegisterChangeTable);


        verticalLayout_7->addWidget(frame_9);

        f_orderPlace = new QFrame(f_orderDashboard);
        f_orderPlace->setObjectName(QString::fromUtf8("f_orderPlace"));
        f_orderPlace->setEnabled(false);
        sizePolicy.setHeightForWidth(f_orderPlace->sizePolicy().hasHeightForWidth());
        f_orderPlace->setSizePolicy(sizePolicy);
        f_orderPlace->setMaximumSize(QSize(2000, 16777215));
        f_orderPlace->setTabletTracking(false);
        f_orderPlace->setStyleSheet(QString::fromUtf8("QRadioButton::indicator::checked\n"
"{\n"
"	border:1px solid black;\n"
"	border-radius: 8px;\n"
"	background-color: gray;\n"
"}\n"
"\n"
"QRadioButton::indicator::unChecked\n"
"{\n"
"	border:1px solid black;\n"
"	border-radius: 8px;\n"
"	background-color: white;\n"
"}"));
        f_orderPlace->setFrameShape(QFrame::StyledPanel);
        f_orderPlace->setFrameShadow(QFrame::Raised);
        horizontalLayout_56 = new QHBoxLayout(f_orderPlace);
        horizontalLayout_56->setObjectName(QString::fromUtf8("horizontalLayout_56"));
        horizontalLayout_56->setContentsMargins(0, 0, 0, 0);
        rb_takeAway = new QRadioButton(f_orderPlace);
        rb_takeAway->setObjectName(QString::fromUtf8("rb_takeAway"));
        rb_takeAway->setEnabled(false);
        sizePolicy.setHeightForWidth(rb_takeAway->sizePolicy().hasHeightForWidth());
        rb_takeAway->setSizePolicy(sizePolicy);
        QFont font1;
        font1.setBold(true);
        rb_takeAway->setFont(font1);
        rb_takeAway->setMouseTracking(true);
        rb_takeAway->setTabletTracking(false);
        QIcon icon19;
        icon19.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-truck-side.svg"), QSize(), QIcon::Normal, QIcon::Off);
        rb_takeAway->setIcon(icon19);
        rb_takeAway->setIconSize(QSize(24, 24));
        rb_takeAway->setCheckable(true);
        rb_takeAway->setChecked(true);

        horizontalLayout_56->addWidget(rb_takeAway);

        rb_onTable = new QRadioButton(f_orderPlace);
        rb_onTable->setObjectName(QString::fromUtf8("rb_onTable"));
        rb_onTable->setEnabled(false);
        sizePolicy.setHeightForWidth(rb_onTable->sizePolicy().hasHeightForWidth());
        rb_onTable->setSizePolicy(sizePolicy);
        QFont font2;
        font2.setBold(true);
        font2.setItalic(false);
        rb_onTable->setFont(font2);
        rb_onTable->setMouseTracking(true);
        rb_onTable->setTabletTracking(false);
        rb_onTable->setIcon(icon2);
        rb_onTable->setIconSize(QSize(24, 24));

        horizontalLayout_56->addWidget(rb_onTable);


        verticalLayout_7->addWidget(f_orderPlace);

        f_cashCommand = new QFrame(f_orderDashboard);
        f_cashCommand->setObjectName(QString::fromUtf8("f_cashCommand"));
        f_cashCommand->setTabletTracking(false);
        f_cashCommand->setFrameShape(QFrame::StyledPanel);
        f_cashCommand->setFrameShadow(QFrame::Raised);
        verticalLayout_9 = new QVBoxLayout(f_cashCommand);
        verticalLayout_9->setSpacing(0);
        verticalLayout_9->setObjectName(QString::fromUtf8("verticalLayout_9"));
        verticalLayout_9->setContentsMargins(0, 0, 0, 5);
        f_orderNav = new QFrame(f_cashCommand);
        f_orderNav->setObjectName(QString::fromUtf8("f_orderNav"));
        f_orderNav->setTabletTracking(false);
        f_orderNav->setFrameShape(QFrame::StyledPanel);
        f_orderNav->setFrameShadow(QFrame::Raised);
        horizontalLayout_6 = new QHBoxLayout(f_orderNav);
        horizontalLayout_6->setSpacing(0);
        horizontalLayout_6->setObjectName(QString::fromUtf8("horizontalLayout_6"));
        horizontalLayout_6->setContentsMargins(0, 0, 0, 0);
        f_ticket = new QFrame(f_orderNav);
        f_ticket->setObjectName(QString::fromUtf8("f_ticket"));
        sizePolicy.setHeightForWidth(f_ticket->sizePolicy().hasHeightForWidth());
        f_ticket->setSizePolicy(sizePolicy);
        f_ticket->setMaximumSize(QSize(40, 16777215));
        f_ticket->setTabletTracking(false);
        f_ticket->setFrameShape(QFrame::StyledPanel);
        f_ticket->setFrameShadow(QFrame::Raised);
        verticalLayout_8 = new QVBoxLayout(f_ticket);
        verticalLayout_8->setSpacing(6);
        verticalLayout_8->setObjectName(QString::fromUtf8("verticalLayout_8"));
        verticalLayout_8->setContentsMargins(0, 0, 0, 0);
        btn_cashRegisterDeleteCurrent = new QPushButton(f_ticket);
        btn_cashRegisterDeleteCurrent->setObjectName(QString::fromUtf8("btn_cashRegisterDeleteCurrent"));
        QSizePolicy sizePolicy7(QSizePolicy::Maximum, QSizePolicy::Minimum);
        sizePolicy7.setHorizontalStretch(0);
        sizePolicy7.setVerticalStretch(0);
        sizePolicy7.setHeightForWidth(btn_cashRegisterDeleteCurrent->sizePolicy().hasHeightForWidth());
        btn_cashRegisterDeleteCurrent->setSizePolicy(sizePolicy7);
        QFont font3;
        font3.setFamilies({QString::fromUtf8("MS Shell Dlg 2")});
        font3.setPointSize(14);
        font3.setBold(false);
        font3.setItalic(false);
        btn_cashRegisterDeleteCurrent->setFont(font3);
        btn_cashRegisterDeleteCurrent->setTabletTracking(false);
        QIcon icon20;
        icon20.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-delete.svg"), QSize(), QIcon::Normal, QIcon::Off);
        btn_cashRegisterDeleteCurrent->setIcon(icon20);
        btn_cashRegisterDeleteCurrent->setIconSize(QSize(32, 32));

        verticalLayout_8->addWidget(btn_cashRegisterDeleteCurrent);

        btn_cashRegisterClear = new QPushButton(f_ticket);
        btn_cashRegisterClear->setObjectName(QString::fromUtf8("btn_cashRegisterClear"));
        sizePolicy7.setHeightForWidth(btn_cashRegisterClear->sizePolicy().hasHeightForWidth());
        btn_cashRegisterClear->setSizePolicy(sizePolicy7);
        btn_cashRegisterClear->setFont(font3);
        btn_cashRegisterClear->setTabletTracking(false);
        QIcon icon21;
        icon21.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-broom.svg"), QSize(), QIcon::Normal, QIcon::Off);
        btn_cashRegisterClear->setIcon(icon21);
        btn_cashRegisterClear->setIconSize(QSize(32, 32));

        verticalLayout_8->addWidget(btn_cashRegisterClear);

        btn_cashRegisterResume = new QPushButton(f_ticket);
        btn_cashRegisterResume->setObjectName(QString::fromUtf8("btn_cashRegisterResume"));
        sizePolicy7.setHeightForWidth(btn_cashRegisterResume->sizePolicy().hasHeightForWidth());
        btn_cashRegisterResume->setSizePolicy(sizePolicy7);
        btn_cashRegisterResume->setFont(font3);
        btn_cashRegisterResume->setTabletTracking(false);
        QIcon icon22;
        icon22.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-time-fast.svg"), QSize(), QIcon::Normal, QIcon::Off);
        btn_cashRegisterResume->setIcon(icon22);
        btn_cashRegisterResume->setIconSize(QSize(32, 32));

        verticalLayout_8->addWidget(btn_cashRegisterResume);

        btn_cashRegisterHold = new QPushButton(f_ticket);
        btn_cashRegisterHold->setObjectName(QString::fromUtf8("btn_cashRegisterHold"));
        sizePolicy7.setHeightForWidth(btn_cashRegisterHold->sizePolicy().hasHeightForWidth());
        btn_cashRegisterHold->setSizePolicy(sizePolicy7);
        btn_cashRegisterHold->setFont(font3);
        btn_cashRegisterHold->setTabletTracking(false);
        QIcon icon23;
        icon23.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-time-add.svg"), QSize(), QIcon::Normal, QIcon::Off);
        btn_cashRegisterHold->setIcon(icon23);
        btn_cashRegisterHold->setIconSize(QSize(32, 32));

        verticalLayout_8->addWidget(btn_cashRegisterHold);


        horizontalLayout_6->addWidget(f_ticket);

        f_totalInfo = new QFrame(f_orderNav);
        f_totalInfo->setObjectName(QString::fromUtf8("f_totalInfo"));
        f_totalInfo->setTabletTracking(false);
        f_totalInfo->setStyleSheet(QString::fromUtf8("QLCDNumber\n"
"{\n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(238, 238, 238);\n"
"	color: rgb(0, 0, 0);\n"
"}"));
        f_totalInfo->setFrameShape(QFrame::StyledPanel);
        f_totalInfo->setFrameShadow(QFrame::Raised);
        gridLayout_8 = new QGridLayout(f_totalInfo);
        gridLayout_8->setObjectName(QString::fromUtf8("gridLayout_8"));
        l_taxDa = new QLabel(f_totalInfo);
        l_taxDa->setObjectName(QString::fromUtf8("l_taxDa"));
        sizePolicy.setHeightForWidth(l_taxDa->sizePolicy().hasHeightForWidth());
        l_taxDa->setSizePolicy(sizePolicy);
        l_taxDa->setMaximumSize(QSize(40, 16777215));
        l_taxDa->setFont(font3);
        l_taxDa->setTabletTracking(false);
        l_taxDa->setFrameShadow(QFrame::Plain);
        l_taxDa->setAlignment(Qt::AlignCenter);

        gridLayout_8->addWidget(l_taxDa, 1, 2, 1, 1);

        l_totalTtc = new QLabel(f_totalInfo);
        l_totalTtc->setObjectName(QString::fromUtf8("l_totalTtc"));
        sizePolicy6.setHeightForWidth(l_totalTtc->sizePolicy().hasHeightForWidth());
        l_totalTtc->setSizePolicy(sizePolicy6);
        l_totalTtc->setFont(font3);
        l_totalTtc->setTabletTracking(false);
        l_totalTtc->setAlignment(Qt::AlignCenter);

        gridLayout_8->addWidget(l_totalTtc, 2, 0, 1, 1);

        l_da = new QLabel(f_totalInfo);
        l_da->setObjectName(QString::fromUtf8("l_da"));
        sizePolicy.setHeightForWidth(l_da->sizePolicy().hasHeightForWidth());
        l_da->setSizePolicy(sizePolicy);
        l_da->setMaximumSize(QSize(40, 16777215));
        l_da->setFont(font3);
        l_da->setTabletTracking(false);
        l_da->setFrameShadow(QFrame::Plain);
        l_da->setAlignment(Qt::AlignCenter);

        gridLayout_8->addWidget(l_da, 0, 2, 1, 1);

        lcdN_totalHtt = new QLCDNumber(f_totalInfo);
        lcdN_totalHtt->setObjectName(QString::fromUtf8("lcdN_totalHtt"));
        sizePolicy.setHeightForWidth(lcdN_totalHtt->sizePolicy().hasHeightForWidth());
        lcdN_totalHtt->setSizePolicy(sizePolicy);
        QFont font4;
        font4.setBold(false);
        lcdN_totalHtt->setFont(font4);
        lcdN_totalHtt->setTabletTracking(false);
        lcdN_totalHtt->setFrameShape(QFrame::StyledPanel);
        lcdN_totalHtt->setFrameShadow(QFrame::Plain);
        lcdN_totalHtt->setLineWidth(1);
        lcdN_totalHtt->setSmallDecimalPoint(true);
        lcdN_totalHtt->setDigitCount(7);
        lcdN_totalHtt->setProperty("value", QVariant(0.000000000000000));

        gridLayout_8->addWidget(lcdN_totalHtt, 0, 1, 1, 1);

        lcdN_tax = new QLCDNumber(f_totalInfo);
        lcdN_tax->setObjectName(QString::fromUtf8("lcdN_tax"));
        sizePolicy.setHeightForWidth(lcdN_tax->sizePolicy().hasHeightForWidth());
        lcdN_tax->setSizePolicy(sizePolicy);
        lcdN_tax->setFont(font4);
        lcdN_tax->setTabletTracking(false);
        lcdN_tax->setFrameShape(QFrame::StyledPanel);
        lcdN_tax->setFrameShadow(QFrame::Plain);
        lcdN_tax->setLineWidth(1);
        lcdN_tax->setSmallDecimalPoint(true);
        lcdN_tax->setDigitCount(7);
        lcdN_tax->setProperty("value", QVariant(0.000000000000000));

        gridLayout_8->addWidget(lcdN_tax, 1, 1, 1, 1);

        l_totalHtt = new QLabel(f_totalInfo);
        l_totalHtt->setObjectName(QString::fromUtf8("l_totalHtt"));
        sizePolicy6.setHeightForWidth(l_totalHtt->sizePolicy().hasHeightForWidth());
        l_totalHtt->setSizePolicy(sizePolicy6);
        l_totalHtt->setFont(font3);
        l_totalHtt->setTabletTracking(false);
        l_totalHtt->setAlignment(Qt::AlignCenter);

        gridLayout_8->addWidget(l_totalHtt, 0, 0, 1, 1);

        lcdN_totalTtc = new QLCDNumber(f_totalInfo);
        lcdN_totalTtc->setObjectName(QString::fromUtf8("lcdN_totalTtc"));
        sizePolicy.setHeightForWidth(lcdN_totalTtc->sizePolicy().hasHeightForWidth());
        lcdN_totalTtc->setSizePolicy(sizePolicy);
        lcdN_totalTtc->setFont(font4);
        lcdN_totalTtc->setTabletTracking(false);
        lcdN_totalTtc->setFrameShape(QFrame::StyledPanel);
        lcdN_totalTtc->setFrameShadow(QFrame::Plain);
        lcdN_totalTtc->setLineWidth(1);
        lcdN_totalTtc->setSmallDecimalPoint(true);
        lcdN_totalTtc->setDigitCount(7);
        lcdN_totalTtc->setProperty("value", QVariant(0.000000000000000));

        gridLayout_8->addWidget(lcdN_totalTtc, 2, 1, 1, 1);

        l_tax = new QLabel(f_totalInfo);
        l_tax->setObjectName(QString::fromUtf8("l_tax"));
        sizePolicy6.setHeightForWidth(l_tax->sizePolicy().hasHeightForWidth());
        l_tax->setSizePolicy(sizePolicy6);
        l_tax->setFont(font3);
        l_tax->setTabletTracking(false);
        l_tax->setAlignment(Qt::AlignCenter);

        gridLayout_8->addWidget(l_tax, 1, 0, 1, 1);

        l_TtcDa = new QLabel(f_totalInfo);
        l_TtcDa->setObjectName(QString::fromUtf8("l_TtcDa"));
        sizePolicy.setHeightForWidth(l_TtcDa->sizePolicy().hasHeightForWidth());
        l_TtcDa->setSizePolicy(sizePolicy);
        l_TtcDa->setMaximumSize(QSize(40, 16777215));
        l_TtcDa->setFont(font3);
        l_TtcDa->setTabletTracking(false);
        l_TtcDa->setFrameShadow(QFrame::Plain);
        l_TtcDa->setAlignment(Qt::AlignCenter);

        gridLayout_8->addWidget(l_TtcDa, 2, 2, 1, 1);


        horizontalLayout_6->addWidget(f_totalInfo);

        f_cashButtons = new QFrame(f_orderNav);
        f_cashButtons->setObjectName(QString::fromUtf8("f_cashButtons"));
        f_cashButtons->setMaximumSize(QSize(50, 16777215));
        f_cashButtons->setTabletTracking(false);
        f_cashButtons->setFrameShape(QFrame::StyledPanel);
        f_cashButtons->setFrameShadow(QFrame::Raised);
        verticalLayout_15 = new QVBoxLayout(f_cashButtons);
        verticalLayout_15->setObjectName(QString::fromUtf8("verticalLayout_15"));
        verticalLayout_15->setContentsMargins(0, 0, 0, 0);
        btn_cashRegisterReduce = new QPushButton(f_cashButtons);
        btn_cashRegisterReduce->setObjectName(QString::fromUtf8("btn_cashRegisterReduce"));
        sizePolicy4.setHeightForWidth(btn_cashRegisterReduce->sizePolicy().hasHeightForWidth());
        btn_cashRegisterReduce->setSizePolicy(sizePolicy4);
        btn_cashRegisterReduce->setMaximumSize(QSize(50, 16777215));
        btn_cashRegisterReduce->setTabletTracking(false);
        QIcon icon24;
        icon24.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-smile-wink.svg"), QSize(), QIcon::Normal, QIcon::Off);
        btn_cashRegisterReduce->setIcon(icon24);
        btn_cashRegisterReduce->setIconSize(QSize(32, 32));

        verticalLayout_15->addWidget(btn_cashRegisterReduce);

        btn_cashRegisterTicketKitchen = new QPushButton(f_cashButtons);
        btn_cashRegisterTicketKitchen->setObjectName(QString::fromUtf8("btn_cashRegisterTicketKitchen"));
        sizePolicy4.setHeightForWidth(btn_cashRegisterTicketKitchen->sizePolicy().hasHeightForWidth());
        btn_cashRegisterTicketKitchen->setSizePolicy(sizePolicy4);
        btn_cashRegisterTicketKitchen->setMaximumSize(QSize(50, 16777215));
        btn_cashRegisterTicketKitchen->setTabletTracking(false);
        QIcon icon25;
        icon25.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-room-service.svg"), QSize(), QIcon::Normal, QIcon::Off);
        btn_cashRegisterTicketKitchen->setIcon(icon25);
        btn_cashRegisterTicketKitchen->setIconSize(QSize(32, 32));

        verticalLayout_15->addWidget(btn_cashRegisterTicketKitchen);

        btn_cashRegisterTicket = new QPushButton(f_cashButtons);
        btn_cashRegisterTicket->setObjectName(QString::fromUtf8("btn_cashRegisterTicket"));
        sizePolicy4.setHeightForWidth(btn_cashRegisterTicket->sizePolicy().hasHeightForWidth());
        btn_cashRegisterTicket->setSizePolicy(sizePolicy4);
        btn_cashRegisterTicket->setMaximumSize(QSize(50, 16777215));
        btn_cashRegisterTicket->setTabletTracking(false);
        QIcon icon26;
        icon26.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-print.svg"), QSize(), QIcon::Normal, QIcon::Off);
        btn_cashRegisterTicket->setIcon(icon26);
        btn_cashRegisterTicket->setIconSize(QSize(32, 32));

        verticalLayout_15->addWidget(btn_cashRegisterTicket);

        btn_cashRegisterPay = new QPushButton(f_cashButtons);
        btn_cashRegisterPay->setObjectName(QString::fromUtf8("btn_cashRegisterPay"));
        sizePolicy4.setHeightForWidth(btn_cashRegisterPay->sizePolicy().hasHeightForWidth());
        btn_cashRegisterPay->setSizePolicy(sizePolicy4);
        btn_cashRegisterPay->setMaximumSize(QSize(50, 16777215));
        btn_cashRegisterPay->setTabletTracking(false);
        QIcon icon27;
        icon27.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-dollar.svg"), QSize(), QIcon::Normal, QIcon::Off);
        btn_cashRegisterPay->setIcon(icon27);
        btn_cashRegisterPay->setIconSize(QSize(32, 32));

        verticalLayout_15->addWidget(btn_cashRegisterPay);


        horizontalLayout_6->addWidget(f_cashButtons);


        verticalLayout_9->addWidget(f_orderNav);

        f_orderWorker = new QFrame(f_cashCommand);
        f_orderWorker->setObjectName(QString::fromUtf8("f_orderWorker"));
        f_orderWorker->setTabletTracking(false);
        f_orderWorker->setFrameShape(QFrame::StyledPanel);
        f_orderWorker->setFrameShadow(QFrame::Raised);
        horizontalLayout_63 = new QHBoxLayout(f_orderWorker);
        horizontalLayout_63->setSpacing(5);
        horizontalLayout_63->setObjectName(QString::fromUtf8("horizontalLayout_63"));
        horizontalLayout_63->setContentsMargins(0, 0, 0, 0);
        l_orderWorker = new QLabel(f_orderWorker);
        l_orderWorker->setObjectName(QString::fromUtf8("l_orderWorker"));
        sizePolicy6.setHeightForWidth(l_orderWorker->sizePolicy().hasHeightForWidth());
        l_orderWorker->setSizePolicy(sizePolicy6);
        l_orderWorker->setFont(font3);
        l_orderWorker->setTabletTracking(false);

        horizontalLayout_63->addWidget(l_orderWorker);

        cb_orderWorker = new QComboBox(f_orderWorker);
        cb_orderWorker->setObjectName(QString::fromUtf8("cb_orderWorker"));
        cb_orderWorker->setEnabled(false);
        cb_orderWorker->setTabletTracking(false);

        horizontalLayout_63->addWidget(cb_orderWorker);


        verticalLayout_9->addWidget(f_orderWorker);


        verticalLayout_7->addWidget(f_cashCommand);

        f_orderCustomer = new QFrame(f_orderDashboard);
        f_orderCustomer->setObjectName(QString::fromUtf8("f_orderCustomer"));
        f_orderCustomer->setTabletTracking(false);
        f_orderCustomer->setFrameShape(QFrame::StyledPanel);
        f_orderCustomer->setFrameShadow(QFrame::Raised);
        horizontalLayout_7 = new QHBoxLayout(f_orderCustomer);
        horizontalLayout_7->setSpacing(5);
        horizontalLayout_7->setObjectName(QString::fromUtf8("horizontalLayout_7"));
        horizontalLayout_7->setContentsMargins(0, 0, 0, 0);
        l_orderCustomer = new QLabel(f_orderCustomer);
        l_orderCustomer->setObjectName(QString::fromUtf8("l_orderCustomer"));
        sizePolicy6.setHeightForWidth(l_orderCustomer->sizePolicy().hasHeightForWidth());
        l_orderCustomer->setSizePolicy(sizePolicy6);
        l_orderCustomer->setFont(font3);
        l_orderCustomer->setTabletTracking(false);

        horizontalLayout_7->addWidget(l_orderCustomer);

        cb_orderCustomer = new QComboBox(f_orderCustomer);
        cb_orderCustomer->setObjectName(QString::fromUtf8("cb_orderCustomer"));
        cb_orderCustomer->setTabletTracking(false);

        horizontalLayout_7->addWidget(cb_orderCustomer);


        verticalLayout_7->addWidget(f_orderCustomer);

        tw_orderList = new QTableWidget(f_orderDashboard);
        tw_orderList->setObjectName(QString::fromUtf8("tw_orderList"));
        tw_orderList->setMinimumSize(QSize(0, 0));
        tw_orderList->setTabletTracking(false);
        tw_orderList->setLayoutDirection(Qt::LeftToRight);
        tw_orderList->setFrameShape(QFrame::StyledPanel);
        tw_orderList->setFrameShadow(QFrame::Sunken);
        tw_orderList->setEditTriggers(QAbstractItemView::NoEditTriggers);
        tw_orderList->setSelectionMode(QAbstractItemView::SingleSelection);
        tw_orderList->setSelectionBehavior(QAbstractItemView::SelectRows);
        tw_orderList->setTextElideMode(Qt::ElideMiddle);
        tw_orderList->setSortingEnabled(true);
        tw_orderList->verticalHeader()->setProperty("showSortIndicator", QVariant(false));

        verticalLayout_7->addWidget(tw_orderList);

        groupBox_2 = new QGroupBox(f_orderDashboard);
        groupBox_2->setObjectName(QString::fromUtf8("groupBox_2"));
        sizePolicy1.setHeightForWidth(groupBox_2->sizePolicy().hasHeightForWidth());
        groupBox_2->setSizePolicy(sizePolicy1);
        groupBox_2->setMinimumSize(QSize(0, 0));
        QFont font5;
        font5.setPointSize(14);
        groupBox_2->setFont(font5);
        groupBox_2->setTabletTracking(false);
        verticalLayout_50 = new QVBoxLayout(groupBox_2);
        verticalLayout_50->setObjectName(QString::fromUtf8("verticalLayout_50"));
        le_cashRegisterComment = new QTextEdit(groupBox_2);
        le_cashRegisterComment->setObjectName(QString::fromUtf8("le_cashRegisterComment"));
        QSizePolicy sizePolicy8(QSizePolicy::Expanding, QSizePolicy::Maximum);
        sizePolicy8.setHorizontalStretch(0);
        sizePolicy8.setVerticalStretch(0);
        sizePolicy8.setHeightForWidth(le_cashRegisterComment->sizePolicy().hasHeightForWidth());
        le_cashRegisterComment->setSizePolicy(sizePolicy8);
        le_cashRegisterComment->setMaximumSize(QSize(16777215, 100));
        QFont font6;
        font6.setPointSize(12);
        le_cashRegisterComment->setFont(font6);
        le_cashRegisterComment->setTabletTracking(false);

        verticalLayout_50->addWidget(le_cashRegisterComment);


        verticalLayout_7->addWidget(groupBox_2);


        gridLayout_5->addWidget(f_orderDashboard, 0, 1, 1, 1);

        f_foodMenu = new QFrame(page_cashRegister);
        f_foodMenu->setObjectName(QString::fromUtf8("f_foodMenu"));
        f_foodMenu->setTabletTracking(false);
        f_foodMenu->setFrameShape(QFrame::StyledPanel);
        f_foodMenu->setFrameShadow(QFrame::Raised);
        verticalLayout_6 = new QVBoxLayout(f_foodMenu);
        verticalLayout_6->setSpacing(0);
        verticalLayout_6->setObjectName(QString::fromUtf8("verticalLayout_6"));
        verticalLayout_6->setContentsMargins(0, 0, 0, 0);
        tw_foodMenu = new QTabWidget(f_foodMenu);
        tw_foodMenu->setObjectName(QString::fromUtf8("tw_foodMenu"));
        sizePolicy4.setHeightForWidth(tw_foodMenu->sizePolicy().hasHeightForWidth());
        tw_foodMenu->setSizePolicy(sizePolicy4);
        tw_foodMenu->setMinimumSize(QSize(400, 0));
        tw_foodMenu->setTabletTracking(false);
        tw_foodMenu->setStyleSheet(QString::fromUtf8(""));
        tw_foodMenu->setIconSize(QSize(35, 35));
        tab_salade = new QWidget();
        tab_salade->setObjectName(QString::fromUtf8("tab_salade"));
        gridLayout_12 = new QGridLayout(tab_salade);
        gridLayout_12->setObjectName(QString::fromUtf8("gridLayout_12"));
        sa_salade = new QScrollArea(tab_salade);
        sa_salade->setObjectName(QString::fromUtf8("sa_salade"));
        sa_salade->setTabletTracking(false);
        sa_salade->setWidgetResizable(true);
        w_salade = new QWidget();
        w_salade->setObjectName(QString::fromUtf8("w_salade"));
        w_salade->setGeometry(QRect(0, 0, 374, 646));
        gridLayout_13 = new QGridLayout(w_salade);
        gridLayout_13->setObjectName(QString::fromUtf8("gridLayout_13"));
        frame_7 = new QFrame(w_salade);
        frame_7->setObjectName(QString::fromUtf8("frame_7"));
        frame_7->setMaximumSize(QSize(200, 200));
        frame_7->setTabletTracking(false);
        frame_7->setFrameShape(QFrame::Box);
        frame_7->setFrameShadow(QFrame::Plain);
        verticalLayout_57 = new QVBoxLayout(frame_7);
        verticalLayout_57->setObjectName(QString::fromUtf8("verticalLayout_57"));
        label_15 = new QLabel(frame_7);
        label_15->setObjectName(QString::fromUtf8("label_15"));
        label_15->setMaximumSize(QSize(200, 200));
        label_15->setTabletTracking(false);
        label_15->setPixmap(QPixmap(QString::fromUtf8(":/Tab/menu.png")));
        label_15->setScaledContents(true);

        verticalLayout_57->addWidget(label_15);

        label_16 = new QLabel(frame_7);
        label_16->setObjectName(QString::fromUtf8("label_16"));
        label_16->setTabletTracking(false);
        label_16->setAlignment(Qt::AlignCenter);

        verticalLayout_57->addWidget(label_16);

        frame_15 = new QFrame(frame_7);
        frame_15->setObjectName(QString::fromUtf8("frame_15"));
        frame_15->setMaximumSize(QSize(200, 100));
        frame_15->setTabletTracking(false);
        frame_15->setFrameShape(QFrame::StyledPanel);
        frame_15->setFrameShadow(QFrame::Raised);
        horizontalLayout_34 = new QHBoxLayout(frame_15);
        horizontalLayout_34->setSpacing(5);
        horizontalLayout_34->setObjectName(QString::fromUtf8("horizontalLayout_34"));
        horizontalLayout_34->setContentsMargins(0, 0, 0, 0);
        pushButton_38 = new QPushButton(frame_15);
        pushButton_38->setObjectName(QString::fromUtf8("pushButton_38"));
        pushButton_38->setTabletTracking(false);

        horizontalLayout_34->addWidget(pushButton_38);

        pushButton_39 = new QPushButton(frame_15);
        pushButton_39->setObjectName(QString::fromUtf8("pushButton_39"));
        pushButton_39->setTabletTracking(false);

        horizontalLayout_34->addWidget(pushButton_39);


        verticalLayout_57->addWidget(frame_15);


        gridLayout_13->addWidget(frame_7, 0, 0, 1, 1);

        frame_16 = new QFrame(w_salade);
        frame_16->setObjectName(QString::fromUtf8("frame_16"));
        frame_16->setMaximumSize(QSize(200, 200));
        frame_16->setTabletTracking(false);
        frame_16->setFrameShape(QFrame::Box);
        frame_16->setFrameShadow(QFrame::Plain);
        verticalLayout_58 = new QVBoxLayout(frame_16);
        verticalLayout_58->setObjectName(QString::fromUtf8("verticalLayout_58"));
        label_17 = new QLabel(frame_16);
        label_17->setObjectName(QString::fromUtf8("label_17"));
        label_17->setMaximumSize(QSize(200, 200));
        label_17->setTabletTracking(false);
        label_17->setPixmap(QPixmap(QString::fromUtf8(":/Tab/menu.png")));
        label_17->setScaledContents(true);

        verticalLayout_58->addWidget(label_17);

        label_18 = new QLabel(frame_16);
        label_18->setObjectName(QString::fromUtf8("label_18"));
        label_18->setTabletTracking(false);
        label_18->setAlignment(Qt::AlignCenter);

        verticalLayout_58->addWidget(label_18);

        frame_17 = new QFrame(frame_16);
        frame_17->setObjectName(QString::fromUtf8("frame_17"));
        frame_17->setMaximumSize(QSize(200, 100));
        frame_17->setTabletTracking(false);
        frame_17->setFrameShape(QFrame::StyledPanel);
        frame_17->setFrameShadow(QFrame::Raised);
        horizontalLayout_35 = new QHBoxLayout(frame_17);
        horizontalLayout_35->setSpacing(5);
        horizontalLayout_35->setObjectName(QString::fromUtf8("horizontalLayout_35"));
        horizontalLayout_35->setContentsMargins(0, 0, 0, 0);
        pushButton_40 = new QPushButton(frame_17);
        pushButton_40->setObjectName(QString::fromUtf8("pushButton_40"));
        pushButton_40->setTabletTracking(false);

        horizontalLayout_35->addWidget(pushButton_40);

        pushButton_41 = new QPushButton(frame_17);
        pushButton_41->setObjectName(QString::fromUtf8("pushButton_41"));
        pushButton_41->setTabletTracking(false);

        horizontalLayout_35->addWidget(pushButton_41);


        verticalLayout_58->addWidget(frame_17);


        gridLayout_13->addWidget(frame_16, 0, 2, 1, 1);

        frame_39 = new QFrame(w_salade);
        frame_39->setObjectName(QString::fromUtf8("frame_39"));
        frame_39->setMaximumSize(QSize(200, 200));
        frame_39->setTabletTracking(false);
        frame_39->setFrameShape(QFrame::Box);
        frame_39->setFrameShadow(QFrame::Plain);
        verticalLayout_91 = new QVBoxLayout(frame_39);
        verticalLayout_91->setObjectName(QString::fromUtf8("verticalLayout_91"));
        label_32 = new QLabel(frame_39);
        label_32->setObjectName(QString::fromUtf8("label_32"));
        label_32->setMaximumSize(QSize(200, 200));
        label_32->setTabletTracking(false);
        label_32->setPixmap(QPixmap(QString::fromUtf8(":/Tab/menu.png")));
        label_32->setScaledContents(true);

        verticalLayout_91->addWidget(label_32);

        label_33 = new QLabel(frame_39);
        label_33->setObjectName(QString::fromUtf8("label_33"));
        label_33->setTabletTracking(false);
        label_33->setAlignment(Qt::AlignCenter);

        verticalLayout_91->addWidget(label_33);

        frame_42 = new QFrame(frame_39);
        frame_42->setObjectName(QString::fromUtf8("frame_42"));
        frame_42->setMaximumSize(QSize(200, 100));
        frame_42->setTabletTracking(false);
        frame_42->setFrameShape(QFrame::StyledPanel);
        frame_42->setFrameShadow(QFrame::Raised);
        horizontalLayout_68 = new QHBoxLayout(frame_42);
        horizontalLayout_68->setSpacing(5);
        horizontalLayout_68->setObjectName(QString::fromUtf8("horizontalLayout_68"));
        horizontalLayout_68->setContentsMargins(0, 0, 0, 0);
        pushButton_56 = new QPushButton(frame_42);
        pushButton_56->setObjectName(QString::fromUtf8("pushButton_56"));
        pushButton_56->setTabletTracking(false);

        horizontalLayout_68->addWidget(pushButton_56);

        pushButton_57 = new QPushButton(frame_42);
        pushButton_57->setObjectName(QString::fromUtf8("pushButton_57"));
        pushButton_57->setTabletTracking(false);

        horizontalLayout_68->addWidget(pushButton_57);


        verticalLayout_91->addWidget(frame_42);


        gridLayout_13->addWidget(frame_39, 0, 1, 1, 1);

        sa_salade->setWidget(w_salade);

        gridLayout_12->addWidget(sa_salade, 0, 0, 1, 1);

        QIcon icon28;
        icon28.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-salad.svg"), QSize(), QIcon::Normal, QIcon::Off);
        tw_foodMenu->addTab(tab_salade, icon28, QString());
        tab_meal = new QWidget();
        tab_meal->setObjectName(QString::fromUtf8("tab_meal"));
        verticalLayout_10 = new QVBoxLayout(tab_meal);
        verticalLayout_10->setObjectName(QString::fromUtf8("verticalLayout_10"));
        sa_meal = new QScrollArea(tab_meal);
        sa_meal->setObjectName(QString::fromUtf8("sa_meal"));
        sa_meal->setWidgetResizable(true);
        w_meal = new QWidget();
        w_meal->setObjectName(QString::fromUtf8("w_meal"));
        w_meal->setGeometry(QRect(0, 0, 517, 646));
        gridLayout_6 = new QGridLayout(w_meal);
        gridLayout_6->setObjectName(QString::fromUtf8("gridLayout_6"));
        frame_18 = new QFrame(w_meal);
        frame_18->setObjectName(QString::fromUtf8("frame_18"));
        frame_18->setMaximumSize(QSize(200, 200));
        frame_18->setFrameShape(QFrame::Box);
        frame_18->setFrameShadow(QFrame::Plain);
        verticalLayout_59 = new QVBoxLayout(frame_18);
        verticalLayout_59->setObjectName(QString::fromUtf8("verticalLayout_59"));
        label_19 = new QLabel(frame_18);
        label_19->setObjectName(QString::fromUtf8("label_19"));
        label_19->setMaximumSize(QSize(200, 200));
        label_19->setPixmap(QPixmap(QString::fromUtf8(":/Tab/menu.png")));
        label_19->setScaledContents(true);

        verticalLayout_59->addWidget(label_19);

        label_20 = new QLabel(frame_18);
        label_20->setObjectName(QString::fromUtf8("label_20"));
        label_20->setAlignment(Qt::AlignCenter);

        verticalLayout_59->addWidget(label_20);

        frame_19 = new QFrame(frame_18);
        frame_19->setObjectName(QString::fromUtf8("frame_19"));
        frame_19->setMaximumSize(QSize(200, 100));
        frame_19->setFrameShape(QFrame::StyledPanel);
        frame_19->setFrameShadow(QFrame::Raised);
        horizontalLayout_36 = new QHBoxLayout(frame_19);
        horizontalLayout_36->setSpacing(5);
        horizontalLayout_36->setObjectName(QString::fromUtf8("horizontalLayout_36"));
        horizontalLayout_36->setContentsMargins(0, 0, 0, 0);
        pushButton_42 = new QPushButton(frame_19);
        pushButton_42->setObjectName(QString::fromUtf8("pushButton_42"));

        horizontalLayout_36->addWidget(pushButton_42);

        pushButton_43 = new QPushButton(frame_19);
        pushButton_43->setObjectName(QString::fromUtf8("pushButton_43"));

        horizontalLayout_36->addWidget(pushButton_43);


        verticalLayout_59->addWidget(frame_19);


        gridLayout_6->addWidget(frame_18, 0, 0, 1, 1);

        frame_20 = new QFrame(w_meal);
        frame_20->setObjectName(QString::fromUtf8("frame_20"));
        frame_20->setMaximumSize(QSize(200, 200));
        frame_20->setFrameShape(QFrame::Box);
        frame_20->setFrameShadow(QFrame::Plain);
        verticalLayout_60 = new QVBoxLayout(frame_20);
        verticalLayout_60->setObjectName(QString::fromUtf8("verticalLayout_60"));
        label_21 = new QLabel(frame_20);
        label_21->setObjectName(QString::fromUtf8("label_21"));
        label_21->setMaximumSize(QSize(200, 200));
        label_21->setPixmap(QPixmap(QString::fromUtf8(":/Tab/menu.png")));
        label_21->setScaledContents(true);

        verticalLayout_60->addWidget(label_21);

        label_22 = new QLabel(frame_20);
        label_22->setObjectName(QString::fromUtf8("label_22"));
        label_22->setAlignment(Qt::AlignCenter);

        verticalLayout_60->addWidget(label_22);

        frame_21 = new QFrame(frame_20);
        frame_21->setObjectName(QString::fromUtf8("frame_21"));
        frame_21->setMaximumSize(QSize(200, 100));
        frame_21->setFrameShape(QFrame::StyledPanel);
        frame_21->setFrameShadow(QFrame::Raised);
        horizontalLayout_37 = new QHBoxLayout(frame_21);
        horizontalLayout_37->setSpacing(5);
        horizontalLayout_37->setObjectName(QString::fromUtf8("horizontalLayout_37"));
        horizontalLayout_37->setContentsMargins(0, 0, 0, 0);
        pushButton_44 = new QPushButton(frame_21);
        pushButton_44->setObjectName(QString::fromUtf8("pushButton_44"));

        horizontalLayout_37->addWidget(pushButton_44);

        pushButton_45 = new QPushButton(frame_21);
        pushButton_45->setObjectName(QString::fromUtf8("pushButton_45"));

        horizontalLayout_37->addWidget(pushButton_45);


        verticalLayout_60->addWidget(frame_21);


        gridLayout_6->addWidget(frame_20, 0, 1, 1, 1);

        frame_41 = new QFrame(w_meal);
        frame_41->setObjectName(QString::fromUtf8("frame_41"));
        frame_41->setMaximumSize(QSize(200, 200));
        frame_41->setFrameShape(QFrame::Box);
        frame_41->setFrameShadow(QFrame::Plain);
        verticalLayout_90 = new QVBoxLayout(frame_41);
        verticalLayout_90->setObjectName(QString::fromUtf8("verticalLayout_90"));
        label_29 = new QLabel(frame_41);
        label_29->setObjectName(QString::fromUtf8("label_29"));
        label_29->setMaximumSize(QSize(200, 200));
        label_29->setPixmap(QPixmap(QString::fromUtf8(":/Tab/menu.png")));
        label_29->setScaledContents(true);

        verticalLayout_90->addWidget(label_29);

        label_31 = new QLabel(frame_41);
        label_31->setObjectName(QString::fromUtf8("label_31"));
        label_31->setAlignment(Qt::AlignCenter);

        verticalLayout_90->addWidget(label_31);

        frame_44 = new QFrame(frame_41);
        frame_44->setObjectName(QString::fromUtf8("frame_44"));
        frame_44->setMaximumSize(QSize(200, 100));
        frame_44->setFrameShape(QFrame::StyledPanel);
        frame_44->setFrameShadow(QFrame::Raised);
        horizontalLayout_65 = new QHBoxLayout(frame_44);
        horizontalLayout_65->setSpacing(5);
        horizontalLayout_65->setObjectName(QString::fromUtf8("horizontalLayout_65"));
        horizontalLayout_65->setContentsMargins(0, 0, 0, 0);
        pushButton_54 = new QPushButton(frame_44);
        pushButton_54->setObjectName(QString::fromUtf8("pushButton_54"));

        horizontalLayout_65->addWidget(pushButton_54);

        pushButton_55 = new QPushButton(frame_44);
        pushButton_55->setObjectName(QString::fromUtf8("pushButton_55"));

        horizontalLayout_65->addWidget(pushButton_55);


        verticalLayout_90->addWidget(frame_44);


        gridLayout_6->addWidget(frame_41, 0, 2, 1, 1);

        sa_meal->setWidget(w_meal);

        verticalLayout_10->addWidget(sa_meal);

        QIcon icon29;
        icon29.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-utensils.svg"), QSize(), QIcon::Normal, QIcon::Off);
        tw_foodMenu->addTab(tab_meal, icon29, QString());
        tab_pizza = new QWidget();
        tab_pizza->setObjectName(QString::fromUtf8("tab_pizza"));
        verticalLayout_11 = new QVBoxLayout(tab_pizza);
        verticalLayout_11->setObjectName(QString::fromUtf8("verticalLayout_11"));
        sa_pizza = new QScrollArea(tab_pizza);
        sa_pizza->setObjectName(QString::fromUtf8("sa_pizza"));
        sa_pizza->setWidgetResizable(true);
        w_pizza = new QWidget();
        w_pizza->setObjectName(QString::fromUtf8("w_pizza"));
        w_pizza->setGeometry(QRect(0, 0, 517, 646));
        gridLayout_7 = new QGridLayout(w_pizza);
        gridLayout_7->setObjectName(QString::fromUtf8("gridLayout_7"));
        frame = new QFrame(w_pizza);
        frame->setObjectName(QString::fromUtf8("frame"));
        frame->setMaximumSize(QSize(200, 200));
        frame->setFrameShape(QFrame::Box);
        frame->setFrameShadow(QFrame::Plain);
        verticalLayout_43 = new QVBoxLayout(frame);
        verticalLayout_43->setObjectName(QString::fromUtf8("verticalLayout_43"));
        label = new QLabel(frame);
        label->setObjectName(QString::fromUtf8("label"));
        label->setMaximumSize(QSize(200, 200));
        label->setPixmap(QPixmap(QString::fromUtf8(":/Tab/menu.png")));
        label->setScaledContents(true);

        verticalLayout_43->addWidget(label);

        label_5 = new QLabel(frame);
        label_5->setObjectName(QString::fromUtf8("label_5"));
        label_5->setAlignment(Qt::AlignCenter);

        verticalLayout_43->addWidget(label_5);

        frame_2 = new QFrame(frame);
        frame_2->setObjectName(QString::fromUtf8("frame_2"));
        frame_2->setMaximumSize(QSize(200, 100));
        frame_2->setFrameShape(QFrame::StyledPanel);
        frame_2->setFrameShadow(QFrame::Raised);
        horizontalLayout_25 = new QHBoxLayout(frame_2);
        horizontalLayout_25->setSpacing(5);
        horizontalLayout_25->setObjectName(QString::fromUtf8("horizontalLayout_25"));
        horizontalLayout_25->setContentsMargins(0, 0, 0, 0);
        pushButton_4 = new QPushButton(frame_2);
        pushButton_4->setObjectName(QString::fromUtf8("pushButton_4"));

        horizontalLayout_25->addWidget(pushButton_4);

        pushButton_14 = new QPushButton(frame_2);
        pushButton_14->setObjectName(QString::fromUtf8("pushButton_14"));

        horizontalLayout_25->addWidget(pushButton_14);


        verticalLayout_43->addWidget(frame_2);


        gridLayout_7->addWidget(frame, 0, 0, 1, 1);

        frame_3 = new QFrame(w_pizza);
        frame_3->setObjectName(QString::fromUtf8("frame_3"));
        frame_3->setMaximumSize(QSize(200, 200));
        frame_3->setFrameShape(QFrame::Box);
        frame_3->setFrameShadow(QFrame::Plain);
        verticalLayout_44 = new QVBoxLayout(frame_3);
        verticalLayout_44->setObjectName(QString::fromUtf8("verticalLayout_44"));
        label_2 = new QLabel(frame_3);
        label_2->setObjectName(QString::fromUtf8("label_2"));
        label_2->setMaximumSize(QSize(200, 200));
        label_2->setPixmap(QPixmap(QString::fromUtf8(":/Tab/menu.png")));
        label_2->setScaledContents(true);

        verticalLayout_44->addWidget(label_2);

        label_6 = new QLabel(frame_3);
        label_6->setObjectName(QString::fromUtf8("label_6"));
        label_6->setAlignment(Qt::AlignCenter);

        verticalLayout_44->addWidget(label_6);

        frame_4 = new QFrame(frame_3);
        frame_4->setObjectName(QString::fromUtf8("frame_4"));
        frame_4->setMaximumSize(QSize(200, 100));
        frame_4->setFrameShape(QFrame::StyledPanel);
        frame_4->setFrameShadow(QFrame::Raised);
        horizontalLayout_26 = new QHBoxLayout(frame_4);
        horizontalLayout_26->setSpacing(5);
        horizontalLayout_26->setObjectName(QString::fromUtf8("horizontalLayout_26"));
        horizontalLayout_26->setContentsMargins(0, 0, 0, 0);
        pushButton_15 = new QPushButton(frame_4);
        pushButton_15->setObjectName(QString::fromUtf8("pushButton_15"));

        horizontalLayout_26->addWidget(pushButton_15);

        pushButton_16 = new QPushButton(frame_4);
        pushButton_16->setObjectName(QString::fromUtf8("pushButton_16"));

        horizontalLayout_26->addWidget(pushButton_16);


        verticalLayout_44->addWidget(frame_4);


        gridLayout_7->addWidget(frame_3, 0, 1, 1, 1);

        frame_48 = new QFrame(w_pizza);
        frame_48->setObjectName(QString::fromUtf8("frame_48"));
        frame_48->setMaximumSize(QSize(200, 200));
        frame_48->setFrameShape(QFrame::Box);
        frame_48->setFrameShadow(QFrame::Plain);
        verticalLayout_92 = new QVBoxLayout(frame_48);
        verticalLayout_92->setObjectName(QString::fromUtf8("verticalLayout_92"));
        label_3 = new QLabel(frame_48);
        label_3->setObjectName(QString::fromUtf8("label_3"));
        label_3->setMaximumSize(QSize(200, 200));
        label_3->setPixmap(QPixmap(QString::fromUtf8(":/Tab/menu.png")));
        label_3->setScaledContents(true);

        verticalLayout_92->addWidget(label_3);

        label_7 = new QLabel(frame_48);
        label_7->setObjectName(QString::fromUtf8("label_7"));
        label_7->setAlignment(Qt::AlignCenter);

        verticalLayout_92->addWidget(label_7);

        frame_49 = new QFrame(frame_48);
        frame_49->setObjectName(QString::fromUtf8("frame_49"));
        frame_49->setMaximumSize(QSize(200, 100));
        frame_49->setFrameShape(QFrame::StyledPanel);
        frame_49->setFrameShadow(QFrame::Raised);
        horizontalLayout_69 = new QHBoxLayout(frame_49);
        horizontalLayout_69->setSpacing(5);
        horizontalLayout_69->setObjectName(QString::fromUtf8("horizontalLayout_69"));
        horizontalLayout_69->setContentsMargins(0, 0, 0, 0);
        pushButton_17 = new QPushButton(frame_49);
        pushButton_17->setObjectName(QString::fromUtf8("pushButton_17"));

        horizontalLayout_69->addWidget(pushButton_17);

        pushButton_18 = new QPushButton(frame_49);
        pushButton_18->setObjectName(QString::fromUtf8("pushButton_18"));

        horizontalLayout_69->addWidget(pushButton_18);


        verticalLayout_92->addWidget(frame_49);


        gridLayout_7->addWidget(frame_48, 0, 2, 1, 1);

        sa_pizza->setWidget(w_pizza);

        verticalLayout_11->addWidget(sa_pizza);

        QIcon icon30;
        icon30.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-pizza-slice.svg"), QSize(), QIcon::Normal, QIcon::Off);
        tw_foodMenu->addTab(tab_pizza, icon30, QString());
        tab_coldDrink = new QWidget();
        tab_coldDrink->setObjectName(QString::fromUtf8("tab_coldDrink"));
        verticalLayout_12 = new QVBoxLayout(tab_coldDrink);
        verticalLayout_12->setObjectName(QString::fromUtf8("verticalLayout_12"));
        sa_coldDrink = new QScrollArea(tab_coldDrink);
        sa_coldDrink->setObjectName(QString::fromUtf8("sa_coldDrink"));
        sa_coldDrink->setWidgetResizable(true);
        w_coldDrink = new QWidget();
        w_coldDrink->setObjectName(QString::fromUtf8("w_coldDrink"));
        w_coldDrink->setGeometry(QRect(0, 0, 517, 646));
        gridLayout_11 = new QGridLayout(w_coldDrink);
        gridLayout_11->setObjectName(QString::fromUtf8("gridLayout_11"));
        frame_24 = new QFrame(w_coldDrink);
        frame_24->setObjectName(QString::fromUtf8("frame_24"));
        frame_24->setMaximumSize(QSize(200, 200));
        frame_24->setFrameShape(QFrame::Box);
        frame_24->setFrameShadow(QFrame::Plain);
        verticalLayout_62 = new QVBoxLayout(frame_24);
        verticalLayout_62->setObjectName(QString::fromUtf8("verticalLayout_62"));
        label_25 = new QLabel(frame_24);
        label_25->setObjectName(QString::fromUtf8("label_25"));
        label_25->setMaximumSize(QSize(200, 200));
        label_25->setPixmap(QPixmap(QString::fromUtf8(":/Tab/menu.png")));
        label_25->setScaledContents(true);

        verticalLayout_62->addWidget(label_25);

        label_26 = new QLabel(frame_24);
        label_26->setObjectName(QString::fromUtf8("label_26"));
        label_26->setAlignment(Qt::AlignCenter);

        verticalLayout_62->addWidget(label_26);

        frame_25 = new QFrame(frame_24);
        frame_25->setObjectName(QString::fromUtf8("frame_25"));
        frame_25->setMaximumSize(QSize(200, 100));
        frame_25->setFrameShape(QFrame::StyledPanel);
        frame_25->setFrameShadow(QFrame::Raised);
        horizontalLayout_39 = new QHBoxLayout(frame_25);
        horizontalLayout_39->setSpacing(5);
        horizontalLayout_39->setObjectName(QString::fromUtf8("horizontalLayout_39"));
        horizontalLayout_39->setContentsMargins(0, 0, 0, 0);
        pushButton_48 = new QPushButton(frame_25);
        pushButton_48->setObjectName(QString::fromUtf8("pushButton_48"));

        horizontalLayout_39->addWidget(pushButton_48);

        pushButton_49 = new QPushButton(frame_25);
        pushButton_49->setObjectName(QString::fromUtf8("pushButton_49"));

        horizontalLayout_39->addWidget(pushButton_49);


        verticalLayout_62->addWidget(frame_25);


        gridLayout_11->addWidget(frame_24, 0, 1, 1, 1);

        frame_22 = new QFrame(w_coldDrink);
        frame_22->setObjectName(QString::fromUtf8("frame_22"));
        frame_22->setMaximumSize(QSize(200, 200));
        frame_22->setFrameShape(QFrame::Box);
        frame_22->setFrameShadow(QFrame::Plain);
        verticalLayout_61 = new QVBoxLayout(frame_22);
        verticalLayout_61->setObjectName(QString::fromUtf8("verticalLayout_61"));
        label_23 = new QLabel(frame_22);
        label_23->setObjectName(QString::fromUtf8("label_23"));
        label_23->setMaximumSize(QSize(200, 200));
        label_23->setPixmap(QPixmap(QString::fromUtf8(":/Tab/menu.png")));
        label_23->setScaledContents(true);

        verticalLayout_61->addWidget(label_23);

        label_24 = new QLabel(frame_22);
        label_24->setObjectName(QString::fromUtf8("label_24"));
        label_24->setAlignment(Qt::AlignCenter);

        verticalLayout_61->addWidget(label_24);

        frame_23 = new QFrame(frame_22);
        frame_23->setObjectName(QString::fromUtf8("frame_23"));
        frame_23->setMaximumSize(QSize(200, 100));
        frame_23->setFrameShape(QFrame::StyledPanel);
        frame_23->setFrameShadow(QFrame::Raised);
        horizontalLayout_38 = new QHBoxLayout(frame_23);
        horizontalLayout_38->setSpacing(5);
        horizontalLayout_38->setObjectName(QString::fromUtf8("horizontalLayout_38"));
        horizontalLayout_38->setContentsMargins(0, 0, 0, 0);
        pushButton_46 = new QPushButton(frame_23);
        pushButton_46->setObjectName(QString::fromUtf8("pushButton_46"));

        horizontalLayout_38->addWidget(pushButton_46);

        pushButton_47 = new QPushButton(frame_23);
        pushButton_47->setObjectName(QString::fromUtf8("pushButton_47"));

        horizontalLayout_38->addWidget(pushButton_47);


        verticalLayout_61->addWidget(frame_23);


        gridLayout_11->addWidget(frame_22, 0, 0, 1, 1);

        frame_50 = new QFrame(w_coldDrink);
        frame_50->setObjectName(QString::fromUtf8("frame_50"));
        frame_50->setMaximumSize(QSize(200, 200));
        frame_50->setFrameShape(QFrame::Box);
        frame_50->setFrameShadow(QFrame::Plain);
        verticalLayout_95 = new QVBoxLayout(frame_50);
        verticalLayout_95->setObjectName(QString::fromUtf8("verticalLayout_95"));
        label_34 = new QLabel(frame_50);
        label_34->setObjectName(QString::fromUtf8("label_34"));
        label_34->setMaximumSize(QSize(200, 200));
        label_34->setPixmap(QPixmap(QString::fromUtf8(":/Tab/menu.png")));
        label_34->setScaledContents(true);

        verticalLayout_95->addWidget(label_34);

        label_41 = new QLabel(frame_50);
        label_41->setObjectName(QString::fromUtf8("label_41"));
        label_41->setAlignment(Qt::AlignCenter);

        verticalLayout_95->addWidget(label_41);

        frame_51 = new QFrame(frame_50);
        frame_51->setObjectName(QString::fromUtf8("frame_51"));
        frame_51->setMaximumSize(QSize(200, 100));
        frame_51->setFrameShape(QFrame::StyledPanel);
        frame_51->setFrameShadow(QFrame::Raised);
        horizontalLayout_72 = new QHBoxLayout(frame_51);
        horizontalLayout_72->setSpacing(5);
        horizontalLayout_72->setObjectName(QString::fromUtf8("horizontalLayout_72"));
        horizontalLayout_72->setContentsMargins(0, 0, 0, 0);
        pushButton_64 = new QPushButton(frame_51);
        pushButton_64->setObjectName(QString::fromUtf8("pushButton_64"));

        horizontalLayout_72->addWidget(pushButton_64);

        pushButton_65 = new QPushButton(frame_51);
        pushButton_65->setObjectName(QString::fromUtf8("pushButton_65"));

        horizontalLayout_72->addWidget(pushButton_65);


        verticalLayout_95->addWidget(frame_51);


        gridLayout_11->addWidget(frame_50, 0, 2, 1, 1);

        sa_coldDrink->setWidget(w_coldDrink);

        verticalLayout_12->addWidget(sa_coldDrink);

        QIcon icon31;
        icon31.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-drink-alt.svg"), QSize(), QIcon::Normal, QIcon::Off);
        tw_foodMenu->addTab(tab_coldDrink, icon31, QString());
        tab_hotDrink = new QWidget();
        tab_hotDrink->setObjectName(QString::fromUtf8("tab_hotDrink"));
        verticalLayout_13 = new QVBoxLayout(tab_hotDrink);
        verticalLayout_13->setObjectName(QString::fromUtf8("verticalLayout_13"));
        sa_hotDrink = new QScrollArea(tab_hotDrink);
        sa_hotDrink->setObjectName(QString::fromUtf8("sa_hotDrink"));
        sa_hotDrink->setWidgetResizable(true);
        w_hotDrink = new QWidget();
        w_hotDrink->setObjectName(QString::fromUtf8("w_hotDrink"));
        w_hotDrink->setGeometry(QRect(0, 0, 517, 646));
        gridLayout_16 = new QGridLayout(w_hotDrink);
        gridLayout_16->setObjectName(QString::fromUtf8("gridLayout_16"));
        frame_28 = new QFrame(w_hotDrink);
        frame_28->setObjectName(QString::fromUtf8("frame_28"));
        frame_28->setMaximumSize(QSize(200, 200));
        frame_28->setFrameShape(QFrame::Box);
        frame_28->setFrameShadow(QFrame::Plain);
        verticalLayout_67 = new QVBoxLayout(frame_28);
        verticalLayout_67->setObjectName(QString::fromUtf8("verticalLayout_67"));
        label_35 = new QLabel(frame_28);
        label_35->setObjectName(QString::fromUtf8("label_35"));
        label_35->setMaximumSize(QSize(200, 200));
        label_35->setPixmap(QPixmap(QString::fromUtf8(":/Tab/menu.png")));
        label_35->setScaledContents(true);

        verticalLayout_67->addWidget(label_35);

        label_36 = new QLabel(frame_28);
        label_36->setObjectName(QString::fromUtf8("label_36"));
        label_36->setAlignment(Qt::AlignCenter);

        verticalLayout_67->addWidget(label_36);

        frame_30 = new QFrame(frame_28);
        frame_30->setObjectName(QString::fromUtf8("frame_30"));
        frame_30->setMaximumSize(QSize(200, 100));
        frame_30->setFrameShape(QFrame::StyledPanel);
        frame_30->setFrameShadow(QFrame::Raised);
        horizontalLayout_44 = new QHBoxLayout(frame_30);
        horizontalLayout_44->setSpacing(5);
        horizontalLayout_44->setObjectName(QString::fromUtf8("horizontalLayout_44"));
        horizontalLayout_44->setContentsMargins(0, 0, 0, 0);
        pushButton_58 = new QPushButton(frame_30);
        pushButton_58->setObjectName(QString::fromUtf8("pushButton_58"));

        horizontalLayout_44->addWidget(pushButton_58);

        pushButton_59 = new QPushButton(frame_30);
        pushButton_59->setObjectName(QString::fromUtf8("pushButton_59"));

        horizontalLayout_44->addWidget(pushButton_59);


        verticalLayout_67->addWidget(frame_30);


        gridLayout_16->addWidget(frame_28, 0, 1, 1, 1);

        frame_26 = new QFrame(w_hotDrink);
        frame_26->setObjectName(QString::fromUtf8("frame_26"));
        frame_26->setMaximumSize(QSize(200, 200));
        frame_26->setFrameShape(QFrame::Box);
        frame_26->setFrameShadow(QFrame::Plain);
        verticalLayout_63 = new QVBoxLayout(frame_26);
        verticalLayout_63->setObjectName(QString::fromUtf8("verticalLayout_63"));
        label_27 = new QLabel(frame_26);
        label_27->setObjectName(QString::fromUtf8("label_27"));
        label_27->setMaximumSize(QSize(200, 200));
        label_27->setPixmap(QPixmap(QString::fromUtf8(":/Tab/menu.png")));
        label_27->setScaledContents(true);

        verticalLayout_63->addWidget(label_27);

        label_28 = new QLabel(frame_26);
        label_28->setObjectName(QString::fromUtf8("label_28"));
        label_28->setAlignment(Qt::AlignCenter);

        verticalLayout_63->addWidget(label_28);

        frame_27 = new QFrame(frame_26);
        frame_27->setObjectName(QString::fromUtf8("frame_27"));
        frame_27->setMaximumSize(QSize(200, 100));
        frame_27->setFrameShape(QFrame::StyledPanel);
        frame_27->setFrameShadow(QFrame::Raised);
        horizontalLayout_40 = new QHBoxLayout(frame_27);
        horizontalLayout_40->setSpacing(5);
        horizontalLayout_40->setObjectName(QString::fromUtf8("horizontalLayout_40"));
        horizontalLayout_40->setContentsMargins(0, 0, 0, 0);
        pushButton_50 = new QPushButton(frame_27);
        pushButton_50->setObjectName(QString::fromUtf8("pushButton_50"));

        horizontalLayout_40->addWidget(pushButton_50);

        pushButton_51 = new QPushButton(frame_27);
        pushButton_51->setObjectName(QString::fromUtf8("pushButton_51"));

        horizontalLayout_40->addWidget(pushButton_51);


        verticalLayout_63->addWidget(frame_27);


        gridLayout_16->addWidget(frame_26, 0, 0, 1, 1);

        frame_52 = new QFrame(w_hotDrink);
        frame_52->setObjectName(QString::fromUtf8("frame_52"));
        frame_52->setMaximumSize(QSize(200, 200));
        frame_52->setFrameShape(QFrame::Box);
        frame_52->setFrameShadow(QFrame::Plain);
        verticalLayout_96 = new QVBoxLayout(frame_52);
        verticalLayout_96->setObjectName(QString::fromUtf8("verticalLayout_96"));
        label_44 = new QLabel(frame_52);
        label_44->setObjectName(QString::fromUtf8("label_44"));
        label_44->setMaximumSize(QSize(200, 200));
        label_44->setPixmap(QPixmap(QString::fromUtf8(":/Tab/menu.png")));
        label_44->setScaledContents(true);

        verticalLayout_96->addWidget(label_44);

        label_45 = new QLabel(frame_52);
        label_45->setObjectName(QString::fromUtf8("label_45"));
        label_45->setAlignment(Qt::AlignCenter);

        verticalLayout_96->addWidget(label_45);

        frame_53 = new QFrame(frame_52);
        frame_53->setObjectName(QString::fromUtf8("frame_53"));
        frame_53->setMaximumSize(QSize(200, 100));
        frame_53->setFrameShape(QFrame::StyledPanel);
        frame_53->setFrameShadow(QFrame::Raised);
        horizontalLayout_73 = new QHBoxLayout(frame_53);
        horizontalLayout_73->setSpacing(5);
        horizontalLayout_73->setObjectName(QString::fromUtf8("horizontalLayout_73"));
        horizontalLayout_73->setContentsMargins(0, 0, 0, 0);
        pushButton_70 = new QPushButton(frame_53);
        pushButton_70->setObjectName(QString::fromUtf8("pushButton_70"));

        horizontalLayout_73->addWidget(pushButton_70);

        pushButton_71 = new QPushButton(frame_53);
        pushButton_71->setObjectName(QString::fromUtf8("pushButton_71"));

        horizontalLayout_73->addWidget(pushButton_71);


        verticalLayout_96->addWidget(frame_53);


        gridLayout_16->addWidget(frame_52, 0, 2, 1, 1);

        sa_hotDrink->setWidget(w_hotDrink);

        verticalLayout_13->addWidget(sa_hotDrink);

        QIcon icon32;
        icon32.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-coffee.svg"), QSize(), QIcon::Normal, QIcon::Off);
        tw_foodMenu->addTab(tab_hotDrink, icon32, QString());
        tab_dessert = new QWidget();
        tab_dessert->setObjectName(QString::fromUtf8("tab_dessert"));
        verticalLayout_14 = new QVBoxLayout(tab_dessert);
        verticalLayout_14->setObjectName(QString::fromUtf8("verticalLayout_14"));
        sa_dessert = new QScrollArea(tab_dessert);
        sa_dessert->setObjectName(QString::fromUtf8("sa_dessert"));
        sa_dessert->setWidgetResizable(true);
        w_dessert = new QWidget();
        w_dessert->setObjectName(QString::fromUtf8("w_dessert"));
        w_dessert->setGeometry(QRect(0, 0, 517, 646));
        gridLayout_17 = new QGridLayout(w_dessert);
        gridLayout_17->setObjectName(QString::fromUtf8("gridLayout_17"));
        frame_36 = new QFrame(w_dessert);
        frame_36->setObjectName(QString::fromUtf8("frame_36"));
        frame_36->setMaximumSize(QSize(200, 200));
        frame_36->setFrameShape(QFrame::Box);
        frame_36->setFrameShadow(QFrame::Plain);
        verticalLayout_69 = new QVBoxLayout(frame_36);
        verticalLayout_69->setObjectName(QString::fromUtf8("verticalLayout_69"));
        label_39 = new QLabel(frame_36);
        label_39->setObjectName(QString::fromUtf8("label_39"));
        label_39->setMaximumSize(QSize(200, 200));
        label_39->setPixmap(QPixmap(QString::fromUtf8(":/Tab/menu.png")));
        label_39->setScaledContents(true);

        verticalLayout_69->addWidget(label_39);

        label_40 = new QLabel(frame_36);
        label_40->setObjectName(QString::fromUtf8("label_40"));
        label_40->setAlignment(Qt::AlignCenter);

        verticalLayout_69->addWidget(label_40);

        frame_37 = new QFrame(frame_36);
        frame_37->setObjectName(QString::fromUtf8("frame_37"));
        frame_37->setMaximumSize(QSize(200, 100));
        frame_37->setFrameShape(QFrame::StyledPanel);
        frame_37->setFrameShadow(QFrame::Raised);
        horizontalLayout_46 = new QHBoxLayout(frame_37);
        horizontalLayout_46->setSpacing(5);
        horizontalLayout_46->setObjectName(QString::fromUtf8("horizontalLayout_46"));
        horizontalLayout_46->setContentsMargins(0, 0, 0, 0);
        pushButton_62 = new QPushButton(frame_37);
        pushButton_62->setObjectName(QString::fromUtf8("pushButton_62"));

        horizontalLayout_46->addWidget(pushButton_62);

        pushButton_63 = new QPushButton(frame_37);
        pushButton_63->setObjectName(QString::fromUtf8("pushButton_63"));

        horizontalLayout_46->addWidget(pushButton_63);


        verticalLayout_69->addWidget(frame_37);


        gridLayout_17->addWidget(frame_36, 0, 1, 1, 1);

        frame_34 = new QFrame(w_dessert);
        frame_34->setObjectName(QString::fromUtf8("frame_34"));
        frame_34->setMaximumSize(QSize(200, 200));
        frame_34->setFrameShape(QFrame::Box);
        frame_34->setFrameShadow(QFrame::Plain);
        verticalLayout_68 = new QVBoxLayout(frame_34);
        verticalLayout_68->setObjectName(QString::fromUtf8("verticalLayout_68"));
        label_37 = new QLabel(frame_34);
        label_37->setObjectName(QString::fromUtf8("label_37"));
        label_37->setMaximumSize(QSize(200, 200));
        label_37->setPixmap(QPixmap(QString::fromUtf8(":/Tab/menu.png")));
        label_37->setScaledContents(true);

        verticalLayout_68->addWidget(label_37);

        label_38 = new QLabel(frame_34);
        label_38->setObjectName(QString::fromUtf8("label_38"));
        label_38->setAlignment(Qt::AlignCenter);

        verticalLayout_68->addWidget(label_38);

        comboBox = new QComboBox(frame_34);
        comboBox->addItem(QString());
        comboBox->addItem(QString());
        comboBox->addItem(QString());
        comboBox->addItem(QString());
        comboBox->setObjectName(QString::fromUtf8("comboBox"));

        verticalLayout_68->addWidget(comboBox);

        frame_35 = new QFrame(frame_34);
        frame_35->setObjectName(QString::fromUtf8("frame_35"));
        frame_35->setMaximumSize(QSize(200, 100));
        frame_35->setFrameShape(QFrame::StyledPanel);
        frame_35->setFrameShadow(QFrame::Raised);
        horizontalLayout_45 = new QHBoxLayout(frame_35);
        horizontalLayout_45->setSpacing(5);
        horizontalLayout_45->setObjectName(QString::fromUtf8("horizontalLayout_45"));
        horizontalLayout_45->setContentsMargins(0, 0, 0, 0);
        pushButton_60 = new QPushButton(frame_35);
        pushButton_60->setObjectName(QString::fromUtf8("pushButton_60"));

        horizontalLayout_45->addWidget(pushButton_60);

        pushButton_61 = new QPushButton(frame_35);
        pushButton_61->setObjectName(QString::fromUtf8("pushButton_61"));

        horizontalLayout_45->addWidget(pushButton_61);


        verticalLayout_68->addWidget(frame_35);


        gridLayout_17->addWidget(frame_34, 0, 0, 1, 1);

        frame_54 = new QFrame(w_dessert);
        frame_54->setObjectName(QString::fromUtf8("frame_54"));
        frame_54->setMaximumSize(QSize(200, 200));
        frame_54->setFrameShape(QFrame::Box);
        frame_54->setFrameShadow(QFrame::Plain);
        verticalLayout_97 = new QVBoxLayout(frame_54);
        verticalLayout_97->setObjectName(QString::fromUtf8("verticalLayout_97"));
        label_46 = new QLabel(frame_54);
        label_46->setObjectName(QString::fromUtf8("label_46"));
        label_46->setMaximumSize(QSize(200, 200));
        label_46->setPixmap(QPixmap(QString::fromUtf8(":/Tab/menu.png")));
        label_46->setScaledContents(true);

        verticalLayout_97->addWidget(label_46);

        label_47 = new QLabel(frame_54);
        label_47->setObjectName(QString::fromUtf8("label_47"));
        label_47->setAlignment(Qt::AlignCenter);

        verticalLayout_97->addWidget(label_47);

        frame_55 = new QFrame(frame_54);
        frame_55->setObjectName(QString::fromUtf8("frame_55"));
        frame_55->setMaximumSize(QSize(200, 100));
        frame_55->setFrameShape(QFrame::StyledPanel);
        frame_55->setFrameShadow(QFrame::Raised);
        horizontalLayout_74 = new QHBoxLayout(frame_55);
        horizontalLayout_74->setSpacing(5);
        horizontalLayout_74->setObjectName(QString::fromUtf8("horizontalLayout_74"));
        horizontalLayout_74->setContentsMargins(0, 0, 0, 0);
        pushButton_72 = new QPushButton(frame_55);
        pushButton_72->setObjectName(QString::fromUtf8("pushButton_72"));

        horizontalLayout_74->addWidget(pushButton_72);

        pushButton_73 = new QPushButton(frame_55);
        pushButton_73->setObjectName(QString::fromUtf8("pushButton_73"));

        horizontalLayout_74->addWidget(pushButton_73);


        verticalLayout_97->addWidget(frame_55);


        gridLayout_17->addWidget(frame_54, 0, 2, 1, 1);

        sa_dessert->setWidget(w_dessert);

        verticalLayout_14->addWidget(sa_dessert);

        QIcon icon33;
        icon33.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-cake-birthday.svg"), QSize(), QIcon::Normal, QIcon::Off);
        tw_foodMenu->addTab(tab_dessert, icon33, QString());

        verticalLayout_6->addWidget(tw_foodMenu);


        gridLayout_5->addWidget(f_foodMenu, 0, 0, 1, 1);

        sw_content->addWidget(page_cashRegister);
        page_reservation = new QWidget();
        page_reservation->setObjectName(QString::fromUtf8("page_reservation"));
        horizontalLayout_51 = new QHBoxLayout(page_reservation);
        horizontalLayout_51->setObjectName(QString::fromUtf8("horizontalLayout_51"));
        f_reservationInputs = new QFrame(page_reservation);
        f_reservationInputs->setObjectName(QString::fromUtf8("f_reservationInputs"));
        f_reservationInputs->setStyleSheet(QString::fromUtf8("QFrame\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	\n"
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
"}"));
        f_reservationInputs->setFrameShape(QFrame::StyledPanel);
        f_reservationInputs->setFrameShadow(QFrame::Raised);
        verticalLayout_72 = new QVBoxLayout(f_reservationInputs);
        verticalLayout_72->setObjectName(QString::fromUtf8("verticalLayout_72"));
        gb_reservation = new QGroupBox(f_reservationInputs);
        gb_reservation->setObjectName(QString::fromUtf8("gb_reservation"));
        gb_reservation->setFont(font3);
        gb_reservation->setStyleSheet(QString::fromUtf8(""));
        verticalLayout_73 = new QVBoxLayout(gb_reservation);
        verticalLayout_73->setObjectName(QString::fromUtf8("verticalLayout_73"));
        le_reservationName = new QLineEdit(gb_reservation);
        le_reservationName->setObjectName(QString::fromUtf8("le_reservationName"));
        le_reservationName->setMaxLength(20);
        le_reservationName->setClearButtonEnabled(true);

        verticalLayout_73->addWidget(le_reservationName);

        le_reservationPhone = new QLineEdit(gb_reservation);
        le_reservationPhone->setObjectName(QString::fromUtf8("le_reservationPhone"));
        le_reservationPhone->setMaxLength(30);
        le_reservationPhone->setClearButtonEnabled(true);

        verticalLayout_73->addWidget(le_reservationPhone);

        le_reservationNbPerson = new QLineEdit(gb_reservation);
        le_reservationNbPerson->setObjectName(QString::fromUtf8("le_reservationNbPerson"));
        le_reservationNbPerson->setMaxLength(20);
        le_reservationNbPerson->setClearButtonEnabled(true);

        verticalLayout_73->addWidget(le_reservationNbPerson);

        dte_reservation = new QDateTimeEdit(gb_reservation);
        dte_reservation->setObjectName(QString::fromUtf8("dte_reservation"));
        dte_reservation->setFont(font5);
        dte_reservation->setCurrentSection(QDateTimeEdit::YearSection);
        dte_reservation->setCalendarPopup(true);

        verticalLayout_73->addWidget(dte_reservation);

        tw_reservationTable = new QTableWidget(gb_reservation);
        tw_reservationTable->setObjectName(QString::fromUtf8("tw_reservationTable"));
        QFont font7;
        font7.setFamilies({QString::fromUtf8("Times New Roman")});
        font7.setPointSize(18);
        font7.setBold(false);
        font7.setItalic(false);
        tw_reservationTable->setFont(font7);
        tw_reservationTable->setEditTriggers(QAbstractItemView::NoEditTriggers);
        tw_reservationTable->setSelectionMode(QAbstractItemView::SingleSelection);
        tw_reservationTable->setSelectionBehavior(QAbstractItemView::SelectRows);
        tw_reservationTable->horizontalHeader()->setProperty("showSortIndicator", QVariant(true));
        tw_reservationTable->verticalHeader()->setCascadingSectionResizes(true);
        tw_reservationTable->verticalHeader()->setProperty("showSortIndicator", QVariant(false));

        verticalLayout_73->addWidget(tw_reservationTable);


        verticalLayout_72->addWidget(gb_reservation);

        f_expenseDbBtn_5 = new QFrame(f_reservationInputs);
        f_expenseDbBtn_5->setObjectName(QString::fromUtf8("f_expenseDbBtn_5"));
        sizePolicy1.setHeightForWidth(f_expenseDbBtn_5->sizePolicy().hasHeightForWidth());
        f_expenseDbBtn_5->setSizePolicy(sizePolicy1);
        f_expenseDbBtn_5->setFrameShape(QFrame::StyledPanel);
        f_expenseDbBtn_5->setFrameShadow(QFrame::Raised);
        horizontalLayout_50 = new QHBoxLayout(f_expenseDbBtn_5);
        horizontalLayout_50->setSpacing(5);
        horizontalLayout_50->setObjectName(QString::fromUtf8("horizontalLayout_50"));
        horizontalLayout_50->setContentsMargins(0, 0, 0, 0);
        btn_reservationAdd = new QPushButton(f_expenseDbBtn_5);
        btn_reservationAdd->setObjectName(QString::fromUtf8("btn_reservationAdd"));
        QIcon icon34;
        icon34.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-add.svg"), QSize(), QIcon::Normal, QIcon::Off);
        btn_reservationAdd->setIcon(icon34);
        btn_reservationAdd->setIconSize(QSize(32, 32));

        horizontalLayout_50->addWidget(btn_reservationAdd);

        btn_reservationEdit = new QPushButton(f_expenseDbBtn_5);
        btn_reservationEdit->setObjectName(QString::fromUtf8("btn_reservationEdit"));
        btn_reservationEdit->setEnabled(false);
        QIcon icon35;
        icon35.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-edit.svg"), QSize(), QIcon::Normal, QIcon::Off);
        btn_reservationEdit->setIcon(icon35);
        btn_reservationEdit->setIconSize(QSize(32, 32));

        horizontalLayout_50->addWidget(btn_reservationEdit);

        btn_reservationDelete = new QPushButton(f_expenseDbBtn_5);
        btn_reservationDelete->setObjectName(QString::fromUtf8("btn_reservationDelete"));
        btn_reservationDelete->setEnabled(false);
        btn_reservationDelete->setIcon(icon20);
        btn_reservationDelete->setIconSize(QSize(32, 32));

        horizontalLayout_50->addWidget(btn_reservationDelete);

        btn_reservationClear = new QPushButton(f_expenseDbBtn_5);
        btn_reservationClear->setObjectName(QString::fromUtf8("btn_reservationClear"));
        btn_reservationClear->setEnabled(true);
        btn_reservationClear->setIcon(icon21);
        btn_reservationClear->setIconSize(QSize(32, 32));

        horizontalLayout_50->addWidget(btn_reservationClear);


        verticalLayout_72->addWidget(f_expenseDbBtn_5);


        horizontalLayout_51->addWidget(f_reservationInputs);

        f_reservationDb = new QFrame(page_reservation);
        f_reservationDb->setObjectName(QString::fromUtf8("f_reservationDb"));
        f_reservationDb->setStyleSheet(QString::fromUtf8("\n"
"\n"
"\n"
"QComboBox\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}"));
        f_reservationDb->setFrameShape(QFrame::StyledPanel);
        f_reservationDb->setFrameShadow(QFrame::Raised);
        verticalLayout_71 = new QVBoxLayout(f_reservationDb);
        verticalLayout_71->setObjectName(QString::fromUtf8("verticalLayout_71"));
        frame_10 = new QFrame(f_reservationDb);
        frame_10->setObjectName(QString::fromUtf8("frame_10"));
        frame_10->setFrameShape(QFrame::StyledPanel);
        frame_10->setFrameShadow(QFrame::Sunken);
        horizontalLayout_52 = new QHBoxLayout(frame_10);
        horizontalLayout_52->setObjectName(QString::fromUtf8("horizontalLayout_52"));
        cb_reservationSearchType = new QComboBox(frame_10);
        cb_reservationSearchType->addItem(QString());
        cb_reservationSearchType->addItem(QString());
        cb_reservationSearchType->setObjectName(QString::fromUtf8("cb_reservationSearchType"));
        QSizePolicy sizePolicy9(QSizePolicy::MinimumExpanding, QSizePolicy::Fixed);
        sizePolicy9.setHorizontalStretch(0);
        sizePolicy9.setVerticalStretch(0);
        sizePolicy9.setHeightForWidth(cb_reservationSearchType->sizePolicy().hasHeightForWidth());
        cb_reservationSearchType->setSizePolicy(sizePolicy9);

        horizontalLayout_52->addWidget(cb_reservationSearchType);

        le_reservationSearch = new QLineEdit(frame_10);
        le_reservationSearch->setObjectName(QString::fromUtf8("le_reservationSearch"));
        sizePolicy9.setHeightForWidth(le_reservationSearch->sizePolicy().hasHeightForWidth());
        le_reservationSearch->setSizePolicy(sizePolicy9);
        le_reservationSearch->setClearButtonEnabled(true);

        horizontalLayout_52->addWidget(le_reservationSearch);

        btn_reservationSearch = new QPushButton(frame_10);
        btn_reservationSearch->setObjectName(QString::fromUtf8("btn_reservationSearch"));
        QIcon icon36;
        icon36.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-search.svg"), QSize(), QIcon::Normal, QIcon::Off);
        btn_reservationSearch->setIcon(icon36);

        horizontalLayout_52->addWidget(btn_reservationSearch);


        verticalLayout_71->addWidget(frame_10);

        frame_11 = new QFrame(f_reservationDb);
        frame_11->setObjectName(QString::fromUtf8("frame_11"));
        frame_11->setFrameShape(QFrame::StyledPanel);
        frame_11->setFrameShadow(QFrame::Sunken);
        horizontalLayout_53 = new QHBoxLayout(frame_11);
        horizontalLayout_53->setObjectName(QString::fromUtf8("horizontalLayout_53"));
        cb_reservationDate = new QCheckBox(frame_11);
        cb_reservationDate->setObjectName(QString::fromUtf8("cb_reservationDate"));
        QSizePolicy sizePolicy10(QSizePolicy::Maximum, QSizePolicy::Fixed);
        sizePolicy10.setHorizontalStretch(0);
        sizePolicy10.setVerticalStretch(0);
        sizePolicy10.setHeightForWidth(cb_reservationDate->sizePolicy().hasHeightForWidth());
        cb_reservationDate->setSizePolicy(sizePolicy10);
        cb_reservationDate->setFont(font6);

        horizontalLayout_53->addWidget(cb_reservationDate);

        de_reservationSearchDate = new QDateEdit(frame_11);
        de_reservationSearchDate->setObjectName(QString::fromUtf8("de_reservationSearchDate"));
        de_reservationSearchDate->setEnabled(false);
        de_reservationSearchDate->setFont(font5);
        de_reservationSearchDate->setAlignment(Qt::AlignCenter);
        de_reservationSearchDate->setProperty("showGroupSeparator", QVariant(false));
        de_reservationSearchDate->setCurrentSection(QDateTimeEdit::YearSection);
        de_reservationSearchDate->setCalendarPopup(true);

        horizontalLayout_53->addWidget(de_reservationSearchDate);


        verticalLayout_71->addWidget(frame_11);

        tw_reservation = new QTableWidget(f_reservationDb);
        tw_reservation->setObjectName(QString::fromUtf8("tw_reservation"));
        tw_reservation->setFont(font7);
        tw_reservation->setEditTriggers(QAbstractItemView::NoEditTriggers);
        tw_reservation->setSelectionMode(QAbstractItemView::SingleSelection);
        tw_reservation->setSelectionBehavior(QAbstractItemView::SelectRows);
        tw_reservation->horizontalHeader()->setProperty("showSortIndicator", QVariant(true));
        tw_reservation->verticalHeader()->setCascadingSectionResizes(true);
        tw_reservation->verticalHeader()->setProperty("showSortIndicator", QVariant(false));

        verticalLayout_71->addWidget(tw_reservation);


        horizontalLayout_51->addWidget(f_reservationDb);

        sw_content->addWidget(page_reservation);
        page_waste = new QWidget();
        page_waste->setObjectName(QString::fromUtf8("page_waste"));
        horizontalLayout_24 = new QHBoxLayout(page_waste);
        horizontalLayout_24->setObjectName(QString::fromUtf8("horizontalLayout_24"));
        w_wasteCustom = new QFrame(page_waste);
        w_wasteCustom->setObjectName(QString::fromUtf8("w_wasteCustom"));
        w_wasteCustom->setStyleSheet(QString::fromUtf8("QFrame\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	\n"
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
"}"));
        verticalLayout_29 = new QVBoxLayout(w_wasteCustom);
        verticalLayout_29->setObjectName(QString::fromUtf8("verticalLayout_29"));
        groupBox_4 = new QGroupBox(w_wasteCustom);
        groupBox_4->setObjectName(QString::fromUtf8("groupBox_4"));
        groupBox_4->setFont(font5);
        verticalLayout_74 = new QVBoxLayout(groupBox_4);
        verticalLayout_74->setObjectName(QString::fromUtf8("verticalLayout_74"));
        cb_wasteStockWorkerId = new QComboBox(groupBox_4);
        cb_wasteStockWorkerId->setObjectName(QString::fromUtf8("cb_wasteStockWorkerId"));

        verticalLayout_74->addWidget(cb_wasteStockWorkerId);

        le_wasteStockQuantity = new QLineEdit(groupBox_4);
        le_wasteStockQuantity->setObjectName(QString::fromUtf8("le_wasteStockQuantity"));

        verticalLayout_74->addWidget(le_wasteStockQuantity);

        tw_wasteStock = new QTableWidget(groupBox_4);
        tw_wasteStock->setObjectName(QString::fromUtf8("tw_wasteStock"));
        QFont font8;
        font8.setFamilies({QString::fromUtf8("Times New Roman")});
        font8.setPointSize(18);
        tw_wasteStock->setFont(font8);
        tw_wasteStock->setSelectionBehavior(QAbstractItemView::SelectRows);

        verticalLayout_74->addWidget(tw_wasteStock);

        frame_29 = new QFrame(groupBox_4);
        frame_29->setObjectName(QString::fromUtf8("frame_29"));
        QSizePolicy sizePolicy11(QSizePolicy::MinimumExpanding, QSizePolicy::Maximum);
        sizePolicy11.setHorizontalStretch(0);
        sizePolicy11.setVerticalStretch(0);
        sizePolicy11.setHeightForWidth(frame_29->sizePolicy().hasHeightForWidth());
        frame_29->setSizePolicy(sizePolicy11);
        horizontalLayout_30 = new QHBoxLayout(frame_29);
        horizontalLayout_30->setObjectName(QString::fromUtf8("horizontalLayout_30"));
        btn_wasteStockClear = new QPushButton(frame_29);
        btn_wasteStockClear->setObjectName(QString::fromUtf8("btn_wasteStockClear"));
        btn_wasteStockClear->setIcon(icon21);
        btn_wasteStockClear->setIconSize(QSize(32, 32));

        horizontalLayout_30->addWidget(btn_wasteStockClear);

        btn_wasteStockSave = new QPushButton(frame_29);
        btn_wasteStockSave->setObjectName(QString::fromUtf8("btn_wasteStockSave"));
        QIcon icon37;
        icon37.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-pharmacy.svg"), QSize(), QIcon::Normal, QIcon::Off);
        btn_wasteStockSave->setIcon(icon37);
        btn_wasteStockSave->setIconSize(QSize(32, 32));

        horizontalLayout_30->addWidget(btn_wasteStockSave);


        verticalLayout_74->addWidget(frame_29);


        verticalLayout_29->addWidget(groupBox_4);

        groupBox_3 = new QGroupBox(w_wasteCustom);
        groupBox_3->setObjectName(QString::fromUtf8("groupBox_3"));
        groupBox_3->setFont(font5);
        verticalLayout_54 = new QVBoxLayout(groupBox_3);
        verticalLayout_54->setObjectName(QString::fromUtf8("verticalLayout_54"));
        cb_wasteCustomWorkerId = new QComboBox(groupBox_3);
        cb_wasteCustomWorkerId->setObjectName(QString::fromUtf8("cb_wasteCustomWorkerId"));

        verticalLayout_54->addWidget(cb_wasteCustomWorkerId);

        le_wasteCustomName = new QLineEdit(groupBox_3);
        le_wasteCustomName->setObjectName(QString::fromUtf8("le_wasteCustomName"));

        verticalLayout_54->addWidget(le_wasteCustomName);

        cb_wasteCustomCategory = new QComboBox(groupBox_3);
        cb_wasteCustomCategory->setObjectName(QString::fromUtf8("cb_wasteCustomCategory"));

        verticalLayout_54->addWidget(cb_wasteCustomCategory);

        le_wasteCustomQuantity = new QLineEdit(groupBox_3);
        le_wasteCustomQuantity->setObjectName(QString::fromUtf8("le_wasteCustomQuantity"));

        verticalLayout_54->addWidget(le_wasteCustomQuantity);

        le_wasteCustomPrice = new QLineEdit(groupBox_3);
        le_wasteCustomPrice->setObjectName(QString::fromUtf8("le_wasteCustomPrice"));

        verticalLayout_54->addWidget(le_wasteCustomPrice);

        frame1 = new QFrame(groupBox_3);
        frame1->setObjectName(QString::fromUtf8("frame1"));
        sizePolicy11.setHeightForWidth(frame1->sizePolicy().hasHeightForWidth());
        frame1->setSizePolicy(sizePolicy11);
        frame1->setStyleSheet(QString::fromUtf8(""));
        horizontalLayout_29 = new QHBoxLayout(frame1);
        horizontalLayout_29->setObjectName(QString::fromUtf8("horizontalLayout_29"));
        btn_wasteCustomClear = new QPushButton(frame1);
        btn_wasteCustomClear->setObjectName(QString::fromUtf8("btn_wasteCustomClear"));
        btn_wasteCustomClear->setIcon(icon21);
        btn_wasteCustomClear->setIconSize(QSize(32, 32));

        horizontalLayout_29->addWidget(btn_wasteCustomClear);

        btn_wasteCustomSave = new QPushButton(frame1);
        btn_wasteCustomSave->setObjectName(QString::fromUtf8("btn_wasteCustomSave"));
        btn_wasteCustomSave->setIcon(icon37);
        btn_wasteCustomSave->setIconSize(QSize(32, 32));

        horizontalLayout_29->addWidget(btn_wasteCustomSave);


        verticalLayout_54->addWidget(frame1);


        verticalLayout_29->addWidget(groupBox_3);


        horizontalLayout_24->addWidget(w_wasteCustom);

        w_wasteStock = new QFrame(page_waste);
        w_wasteStock->setObjectName(QString::fromUtf8("w_wasteStock"));
        w_wasteStock->setMinimumSize(QSize(200, 0));
        w_wasteStock->setStyleSheet(QString::fromUtf8("QFrame\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	\n"
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
"}"));
        verticalLayout_36 = new QVBoxLayout(w_wasteStock);
        verticalLayout_36->setObjectName(QString::fromUtf8("verticalLayout_36"));
        tw_waste = new QTableWidget(w_wasteStock);
        tw_waste->setObjectName(QString::fromUtf8("tw_waste"));
        tw_waste->setFont(font8);
        tw_waste->setSelectionBehavior(QAbstractItemView::SelectRows);

        verticalLayout_36->addWidget(tw_waste);


        horizontalLayout_24->addWidget(w_wasteStock);

        sw_content->addWidget(page_waste);
        page_overview = new QWidget();
        page_overview->setObjectName(QString::fromUtf8("page_overview"));
        horizontalLayout_33 = new QHBoxLayout(page_overview);
        horizontalLayout_33->setObjectName(QString::fromUtf8("horizontalLayout_33"));
        frame_12 = new QFrame(page_overview);
        frame_12->setObjectName(QString::fromUtf8("frame_12"));
        frame_12->setStyleSheet(QString::fromUtf8("QFrame\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	\n"
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
"}"));
        frame_12->setFrameShape(QFrame::StyledPanel);
        frame_12->setFrameShadow(QFrame::Raised);
        verticalLayout_49 = new QVBoxLayout(frame_12);
        verticalLayout_49->setObjectName(QString::fromUtf8("verticalLayout_49"));
        l_stock = new QLabel(frame_12);
        l_stock->setObjectName(QString::fromUtf8("l_stock"));
        QFont font9;
        font9.setPointSize(14);
        font9.setBold(true);
        font9.setUnderline(true);
        l_stock->setFont(font9);
        l_stock->setAlignment(Qt::AlignCenter);

        verticalLayout_49->addWidget(l_stock);

        frame_38 = new QFrame(frame_12);
        frame_38->setObjectName(QString::fromUtf8("frame_38"));
        frame_38->setFrameShape(QFrame::StyledPanel);
        frame_38->setFrameShadow(QFrame::Plain);
        horizontalLayout_57 = new QHBoxLayout(frame_38);
        horizontalLayout_57->setObjectName(QString::fromUtf8("horizontalLayout_57"));
        rb_stockIngredients = new QRadioButton(frame_38);
        rb_stockIngredients->setObjectName(QString::fromUtf8("rb_stockIngredients"));
        rb_stockIngredients->setFont(font6);
        rb_stockIngredients->setChecked(true);

        horizontalLayout_57->addWidget(rb_stockIngredients);

        rb_stockOthers = new QRadioButton(frame_38);
        rb_stockOthers->setObjectName(QString::fromUtf8("rb_stockOthers"));
        rb_stockOthers->setFont(font6);

        horizontalLayout_57->addWidget(rb_stockOthers);


        verticalLayout_49->addWidget(frame_38);

        tw_stock = new QTableWidget(frame_12);
        tw_stock->setObjectName(QString::fromUtf8("tw_stock"));
        QFont font10;
        font10.setFamilies({QString::fromUtf8("Times New Roman")});
        font10.setPointSize(22);
        tw_stock->setFont(font10);
        tw_stock->setSelectionBehavior(QAbstractItemView::SelectRows);

        verticalLayout_49->addWidget(tw_stock);


        horizontalLayout_33->addWidget(frame_12);

        sw_content->addWidget(page_overview);
        page_productReceipt = new QWidget();
        page_productReceipt->setObjectName(QString::fromUtf8("page_productReceipt"));
        gridLayout_14 = new QGridLayout(page_productReceipt);
        gridLayout_14->setObjectName(QString::fromUtf8("gridLayout_14"));
        frame_6 = new QFrame(page_productReceipt);
        frame_6->setObjectName(QString::fromUtf8("frame_6"));
        frame_6->setStyleSheet(QString::fromUtf8("QFrame\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	\n"
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
"}"));
        frame_6->setFrameShape(QFrame::StyledPanel);
        frame_6->setFrameShadow(QFrame::Raised);
        verticalLayout_48 = new QVBoxLayout(frame_6);
        verticalLayout_48->setObjectName(QString::fromUtf8("verticalLayout_48"));
        l_productReceiptSelection = new QLabel(frame_6);
        l_productReceiptSelection->setObjectName(QString::fromUtf8("l_productReceiptSelection"));
        QFont font11;
        font11.setFamilies({QString::fromUtf8("Times New Roman")});
        font11.setPointSize(14);
        font11.setBold(true);
        l_productReceiptSelection->setFont(font11);

        verticalLayout_48->addWidget(l_productReceiptSelection);

        frame_14 = new QFrame(frame_6);
        frame_14->setObjectName(QString::fromUtf8("frame_14"));
        frame_14->setFrameShape(QFrame::StyledPanel);
        frame_14->setFrameShadow(QFrame::Sunken);
        gridLayout_22 = new QGridLayout(frame_14);
        gridLayout_22->setObjectName(QString::fromUtf8("gridLayout_22"));
        l_ingredient_2 = new QLabel(frame_14);
        l_ingredient_2->setObjectName(QString::fromUtf8("l_ingredient_2"));
        sizePolicy.setHeightForWidth(l_ingredient_2->sizePolicy().hasHeightForWidth());
        l_ingredient_2->setSizePolicy(sizePolicy);
        QFont font12;
        font12.setFamilies({QString::fromUtf8("Times New Roman")});
        font12.setPointSize(14);
        l_ingredient_2->setFont(font12);
        l_ingredient_2->setAlignment(Qt::AlignCenter);
        l_ingredient_2->setMargin(5);

        gridLayout_22->addWidget(l_ingredient_2, 2, 0, 1, 1);

        cb_productReceiptMenuItem = new QComboBox(frame_14);
        cb_productReceiptMenuItem->setObjectName(QString::fromUtf8("cb_productReceiptMenuItem"));
        sizePolicy9.setHeightForWidth(cb_productReceiptMenuItem->sizePolicy().hasHeightForWidth());
        cb_productReceiptMenuItem->setSizePolicy(sizePolicy9);

        gridLayout_22->addWidget(cb_productReceiptMenuItem, 2, 1, 1, 1);


        verticalLayout_48->addWidget(frame_14);

        frame_8 = new QFrame(frame_6);
        frame_8->setObjectName(QString::fromUtf8("frame_8"));
        frame_8->setInputMethodHints(Qt::ImhDigitsOnly);
        frame_8->setFrameShape(QFrame::StyledPanel);
        frame_8->setFrameShadow(QFrame::Sunken);
        gridLayout_15 = new QGridLayout(frame_8);
        gridLayout_15->setObjectName(QString::fromUtf8("gridLayout_15"));
        btn_productReceiptAdd = new QPushButton(frame_8);
        btn_productReceiptAdd->setObjectName(QString::fromUtf8("btn_productReceiptAdd"));
        btn_productReceiptAdd->setIcon(icon34);
        btn_productReceiptAdd->setIconSize(QSize(32, 32));

        gridLayout_15->addWidget(btn_productReceiptAdd, 1, 3, 1, 1);

        cb_productReceiptIngredientName = new QComboBox(frame_8);
        cb_productReceiptIngredientName->setObjectName(QString::fromUtf8("cb_productReceiptIngredientName"));
        sizePolicy9.setHeightForWidth(cb_productReceiptIngredientName->sizePolicy().hasHeightForWidth());
        cb_productReceiptIngredientName->setSizePolicy(sizePolicy9);

        gridLayout_15->addWidget(cb_productReceiptIngredientName, 1, 1, 1, 1);

        btn_productReceiptRemove = new QPushButton(frame_8);
        btn_productReceiptRemove->setObjectName(QString::fromUtf8("btn_productReceiptRemove"));
        btn_productReceiptRemove->setEnabled(false);
        QIcon icon38;
        icon38.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-cross-circle.svg"), QSize(), QIcon::Normal, QIcon::Off);
        btn_productReceiptRemove->setIcon(icon38);
        btn_productReceiptRemove->setIconSize(QSize(32, 32));

        gridLayout_15->addWidget(btn_productReceiptRemove, 1, 5, 1, 1);

        le_productReceiptIngredientQuantity = new QLineEdit(frame_8);
        le_productReceiptIngredientQuantity->setObjectName(QString::fromUtf8("le_productReceiptIngredientQuantity"));
        sizePolicy5.setHeightForWidth(le_productReceiptIngredientQuantity->sizePolicy().hasHeightForWidth());
        le_productReceiptIngredientQuantity->setSizePolicy(sizePolicy5);
        le_productReceiptIngredientQuantity->setInputMethodHints(Qt::ImhDigitsOnly|Qt::ImhFormattedNumbersOnly);
        le_productReceiptIngredientQuantity->setClearButtonEnabled(true);

        gridLayout_15->addWidget(le_productReceiptIngredientQuantity, 1, 2, 1, 1);

        btn_productReceiptEdit = new QPushButton(frame_8);
        btn_productReceiptEdit->setObjectName(QString::fromUtf8("btn_productReceiptEdit"));
        btn_productReceiptEdit->setEnabled(false);
        btn_productReceiptEdit->setIcon(icon35);
        btn_productReceiptEdit->setIconSize(QSize(32, 32));

        gridLayout_15->addWidget(btn_productReceiptEdit, 1, 4, 1, 1);

        l_ingredient = new QLabel(frame_8);
        l_ingredient->setObjectName(QString::fromUtf8("l_ingredient"));
        sizePolicy.setHeightForWidth(l_ingredient->sizePolicy().hasHeightForWidth());
        l_ingredient->setSizePolicy(sizePolicy);
        l_ingredient->setFont(font12);
        l_ingredient->setAlignment(Qt::AlignCenter);
        l_ingredient->setMargin(5);

        gridLayout_15->addWidget(l_ingredient, 1, 0, 1, 1);

        btn_productReceiptClear = new QPushButton(frame_8);
        btn_productReceiptClear->setObjectName(QString::fromUtf8("btn_productReceiptClear"));
        btn_productReceiptClear->setEnabled(true);
        btn_productReceiptClear->setIcon(icon21);
        btn_productReceiptClear->setIconSize(QSize(32, 32));

        gridLayout_15->addWidget(btn_productReceiptClear, 1, 6, 1, 1);


        verticalLayout_48->addWidget(frame_8);

        tw_productReceiptIngredientList = new QTableWidget(frame_6);
        tw_productReceiptIngredientList->setObjectName(QString::fromUtf8("tw_productReceiptIngredientList"));
        tw_productReceiptIngredientList->setFont(font10);
        tw_productReceiptIngredientList->setSelectionBehavior(QAbstractItemView::SelectRows);

        verticalLayout_48->addWidget(tw_productReceiptIngredientList);

        frame_31 = new QFrame(frame_6);
        frame_31->setObjectName(QString::fromUtf8("frame_31"));
        frame_31->setFrameShape(QFrame::StyledPanel);
        frame_31->setFrameShadow(QFrame::Sunken);
        gridLayout_23 = new QGridLayout(frame_31);
        gridLayout_23->setObjectName(QString::fromUtf8("gridLayout_23"));
        l_ingredient_7 = new QLabel(frame_31);
        l_ingredient_7->setObjectName(QString::fromUtf8("l_ingredient_7"));
        sizePolicy.setHeightForWidth(l_ingredient_7->sizePolicy().hasHeightForWidth());
        l_ingredient_7->setSizePolicy(sizePolicy);
        l_ingredient_7->setFont(font11);
        l_ingredient_7->setAlignment(Qt::AlignCenter);
        l_ingredient_7->setMargin(5);

        gridLayout_23->addWidget(l_ingredient_7, 2, 2, 1, 1);

        l_ingredient_5 = new QLabel(frame_31);
        l_ingredient_5->setObjectName(QString::fromUtf8("l_ingredient_5"));
        sizePolicy.setHeightForWidth(l_ingredient_5->sizePolicy().hasHeightForWidth());
        l_ingredient_5->setSizePolicy(sizePolicy);
        l_ingredient_5->setFont(font11);
        l_ingredient_5->setAlignment(Qt::AlignCenter);
        l_ingredient_5->setMargin(5);

        gridLayout_23->addWidget(l_ingredient_5, 2, 0, 1, 1);

        l_ingredient_8 = new QLabel(frame_31);
        l_ingredient_8->setObjectName(QString::fromUtf8("l_ingredient_8"));
        sizePolicy.setHeightForWidth(l_ingredient_8->sizePolicy().hasHeightForWidth());
        l_ingredient_8->setSizePolicy(sizePolicy);
        l_ingredient_8->setFont(font11);
        l_ingredient_8->setAlignment(Qt::AlignCenter);
        l_ingredient_8->setMargin(5);

        gridLayout_23->addWidget(l_ingredient_8, 2, 3, 1, 1);

        l_productReceiptQuantity = new QLabel(frame_31);
        l_productReceiptQuantity->setObjectName(QString::fromUtf8("l_productReceiptQuantity"));
        sizePolicy.setHeightForWidth(l_productReceiptQuantity->sizePolicy().hasHeightForWidth());
        l_productReceiptQuantity->setSizePolicy(sizePolicy);
        l_productReceiptQuantity->setFont(font12);
        l_productReceiptQuantity->setAlignment(Qt::AlignCenter);
        l_productReceiptQuantity->setMargin(5);

        gridLayout_23->addWidget(l_productReceiptQuantity, 3, 3, 1, 1);

        l_productReceiptPrice = new QLabel(frame_31);
        l_productReceiptPrice->setObjectName(QString::fromUtf8("l_productReceiptPrice"));
        sizePolicy.setHeightForWidth(l_productReceiptPrice->sizePolicy().hasHeightForWidth());
        l_productReceiptPrice->setSizePolicy(sizePolicy);
        l_productReceiptPrice->setFont(font12);
        l_productReceiptPrice->setAlignment(Qt::AlignCenter);
        l_productReceiptPrice->setMargin(5);

        gridLayout_23->addWidget(l_productReceiptPrice, 3, 2, 1, 1);

        l_productReceiptEstimatedProductionPrice = new QLabel(frame_31);
        l_productReceiptEstimatedProductionPrice->setObjectName(QString::fromUtf8("l_productReceiptEstimatedProductionPrice"));
        sizePolicy.setHeightForWidth(l_productReceiptEstimatedProductionPrice->sizePolicy().hasHeightForWidth());
        l_productReceiptEstimatedProductionPrice->setSizePolicy(sizePolicy);
        l_productReceiptEstimatedProductionPrice->setFont(font12);
        l_productReceiptEstimatedProductionPrice->setAlignment(Qt::AlignCenter);
        l_productReceiptEstimatedProductionPrice->setMargin(5);

        gridLayout_23->addWidget(l_productReceiptEstimatedProductionPrice, 3, 0, 1, 1);


        verticalLayout_48->addWidget(frame_31);


        gridLayout_14->addWidget(frame_6, 0, 0, 1, 1);

        sw_content->addWidget(page_productReceipt);
        page_database = new QWidget();
        page_database->setObjectName(QString::fromUtf8("page_database"));
        gridLayout_9 = new QGridLayout(page_database);
        gridLayout_9->setSpacing(0);
        gridLayout_9->setObjectName(QString::fromUtf8("gridLayout_9"));
        gridLayout_9->setContentsMargins(0, 0, 0, 0);
        tw_database = new QTabWidget(page_database);
        tw_database->setObjectName(QString::fromUtf8("tw_database"));
        QFont font13;
        font13.setPointSize(18);
        tw_database->setFont(font13);
        tw_database->setIconSize(QSize(35, 35));
        tab_menu = new QWidget();
        tab_menu->setObjectName(QString::fromUtf8("tab_menu"));
        horizontalLayout_8 = new QHBoxLayout(tab_menu);
        horizontalLayout_8->setObjectName(QString::fromUtf8("horizontalLayout_8"));
        f_menuItemInputs = new QFrame(tab_menu);
        f_menuItemInputs->setObjectName(QString::fromUtf8("f_menuItemInputs"));
        f_menuItemInputs->setMaximumSize(QSize(800, 16777215));
        f_menuItemInputs->setStyleSheet(QString::fromUtf8("QFrame\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	\n"
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
"}"));
        f_menuItemInputs->setFrameShape(QFrame::StyledPanel);
        f_menuItemInputs->setFrameShadow(QFrame::Raised);
        verticalLayout_18 = new QVBoxLayout(f_menuItemInputs);
        verticalLayout_18->setObjectName(QString::fromUtf8("verticalLayout_18"));
        verticalLayout_18->setContentsMargins(9, -1, -1, -1);
        gb_menuItem = new QGroupBox(f_menuItemInputs);
        gb_menuItem->setObjectName(QString::fromUtf8("gb_menuItem"));
        gb_menuItem->setFont(font5);
        gb_menuItem->setStyleSheet(QString::fromUtf8("QLineEdit\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
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
""));
        verticalLayout_19 = new QVBoxLayout(gb_menuItem);
        verticalLayout_19->setSpacing(0);
        verticalLayout_19->setObjectName(QString::fromUtf8("verticalLayout_19"));
        verticalLayout_19->setContentsMargins(0, 0, 0, 0);
        f_menuItemPic = new QFrame(gb_menuItem);
        f_menuItemPic->setObjectName(QString::fromUtf8("f_menuItemPic"));
        QSizePolicy sizePolicy12(QSizePolicy::Maximum, QSizePolicy::Maximum);
        sizePolicy12.setHorizontalStretch(0);
        sizePolicy12.setVerticalStretch(0);
        sizePolicy12.setHeightForWidth(f_menuItemPic->sizePolicy().hasHeightForWidth());
        f_menuItemPic->setSizePolicy(sizePolicy12);
        f_menuItemPic->setMinimumSize(QSize(200, 200));
        f_menuItemPic->setMaximumSize(QSize(800, 300));
        f_menuItemPic->setLayoutDirection(Qt::LeftToRight);
        f_menuItemPic->setStyleSheet(QString::fromUtf8(""));
        f_menuItemPic->setFrameShape(QFrame::StyledPanel);
        f_menuItemPic->setFrameShadow(QFrame::Raised);
        horizontalLayout_17 = new QHBoxLayout(f_menuItemPic);
        horizontalLayout_17->setSpacing(0);
        horizontalLayout_17->setObjectName(QString::fromUtf8("horizontalLayout_17"));
        horizontalLayout_17->setSizeConstraint(QLayout::SetMinimumSize);
        horizontalLayout_17->setContentsMargins(0, 0, 0, 0);
        l_menuItemPicture = new QLabel(f_menuItemPic);
        l_menuItemPicture->setObjectName(QString::fromUtf8("l_menuItemPicture"));
        sizePolicy.setHeightForWidth(l_menuItemPicture->sizePolicy().hasHeightForWidth());
        l_menuItemPicture->setSizePolicy(sizePolicy);
        l_menuItemPicture->setMinimumSize(QSize(250, 200));
        l_menuItemPicture->setMaximumSize(QSize(300, 300));
        l_menuItemPicture->setBaseSize(QSize(200, 200));
        QFont font14;
        font14.setPointSize(20);
        l_menuItemPicture->setFont(font14);
        l_menuItemPicture->setLayoutDirection(Qt::LeftToRight);
        l_menuItemPicture->setAutoFillBackground(false);
        l_menuItemPicture->setStyleSheet(QString::fromUtf8(""));
        l_menuItemPicture->setFrameShape(QFrame::Box);
        l_menuItemPicture->setFrameShadow(QFrame::Plain);
        l_menuItemPicture->setScaledContents(true);
        l_menuItemPicture->setAlignment(Qt::AlignCenter);
        l_menuItemPicture->setWordWrap(false);

        horizontalLayout_17->addWidget(l_menuItemPicture);

        f_finishProductPictureSetting = new QFrame(f_menuItemPic);
        f_finishProductPictureSetting->setObjectName(QString::fromUtf8("f_finishProductPictureSetting"));
        f_finishProductPictureSetting->setFrameShape(QFrame::StyledPanel);
        f_finishProductPictureSetting->setFrameShadow(QFrame::Raised);
        verticalLayout_41 = new QVBoxLayout(f_finishProductPictureSetting);
        verticalLayout_41->setObjectName(QString::fromUtf8("verticalLayout_41"));
        btn_menuItemPicture = new QPushButton(f_finishProductPictureSetting);
        btn_menuItemPicture->setObjectName(QString::fromUtf8("btn_menuItemPicture"));
        sizePolicy12.setHeightForWidth(btn_menuItemPicture->sizePolicy().hasHeightForWidth());
        btn_menuItemPicture->setSizePolicy(sizePolicy12);
        QIcon icon39;
        icon39.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-picture.svg"), QSize(), QIcon::Normal, QIcon::Off);
        btn_menuItemPicture->setIcon(icon39);
        btn_menuItemPicture->setIconSize(QSize(32, 32));

        verticalLayout_41->addWidget(btn_menuItemPicture);

        btn_menuItemPictureClear = new QPushButton(f_finishProductPictureSetting);
        btn_menuItemPictureClear->setObjectName(QString::fromUtf8("btn_menuItemPictureClear"));
        sizePolicy12.setHeightForWidth(btn_menuItemPictureClear->sizePolicy().hasHeightForWidth());
        btn_menuItemPictureClear->setSizePolicy(sizePolicy12);
        btn_menuItemPictureClear->setIcon(icon21);
        btn_menuItemPictureClear->setIconSize(QSize(32, 32));

        verticalLayout_41->addWidget(btn_menuItemPictureClear);


        horizontalLayout_17->addWidget(f_finishProductPictureSetting);


        verticalLayout_19->addWidget(f_menuItemPic);

        le_menuItemName = new QLineEdit(gb_menuItem);
        le_menuItemName->setObjectName(QString::fromUtf8("le_menuItemName"));
        le_menuItemName->setMaxLength(150);
        le_menuItemName->setClearButtonEnabled(true);

        verticalLayout_19->addWidget(le_menuItemName);

        cb_menuItemCategory = new QComboBox(gb_menuItem);
        cb_menuItemCategory->addItem(QString());
        cb_menuItemCategory->addItem(QString());
        cb_menuItemCategory->addItem(QString());
        cb_menuItemCategory->addItem(QString());
        cb_menuItemCategory->addItem(QString());
        cb_menuItemCategory->addItem(QString());
        cb_menuItemCategory->setObjectName(QString::fromUtf8("cb_menuItemCategory"));
        cb_menuItemCategory->setFrame(true);

        verticalLayout_19->addWidget(cb_menuItemCategory);

        cb_menuItemCategoryCustom = new QComboBox(gb_menuItem);
        cb_menuItemCategoryCustom->setObjectName(QString::fromUtf8("cb_menuItemCategoryCustom"));

        verticalLayout_19->addWidget(cb_menuItemCategoryCustom);

        le_menuItemUnit = new QLineEdit(gb_menuItem);
        le_menuItemUnit->setObjectName(QString::fromUtf8("le_menuItemUnit"));

        verticalLayout_19->addWidget(le_menuItemUnit);

        le_menuItemUnitQuantity = new QLineEdit(gb_menuItem);
        le_menuItemUnitQuantity->setObjectName(QString::fromUtf8("le_menuItemUnitQuantity"));
        le_menuItemUnitQuantity->setMaxLength(20);
        le_menuItemUnitQuantity->setClearButtonEnabled(true);

        verticalLayout_19->addWidget(le_menuItemUnitQuantity);

        le_menuItemPrice = new QLineEdit(gb_menuItem);
        le_menuItemPrice->setObjectName(QString::fromUtf8("le_menuItemPrice"));
        le_menuItemPrice->setMaxLength(20);
        le_menuItemPrice->setClearButtonEnabled(true);

        verticalLayout_19->addWidget(le_menuItemPrice);


        verticalLayout_18->addWidget(gb_menuItem);

        f_menuItemDbBtn = new QFrame(f_menuItemInputs);
        f_menuItemDbBtn->setObjectName(QString::fromUtf8("f_menuItemDbBtn"));
        sizePolicy1.setHeightForWidth(f_menuItemDbBtn->sizePolicy().hasHeightForWidth());
        f_menuItemDbBtn->setSizePolicy(sizePolicy1);
        f_menuItemDbBtn->setFrameShape(QFrame::StyledPanel);
        f_menuItemDbBtn->setFrameShadow(QFrame::Raised);
        horizontalLayout_16 = new QHBoxLayout(f_menuItemDbBtn);
        horizontalLayout_16->setSpacing(5);
        horizontalLayout_16->setObjectName(QString::fromUtf8("horizontalLayout_16"));
        horizontalLayout_16->setContentsMargins(0, 0, 0, 0);
        btn_menuItemAdd = new QPushButton(f_menuItemDbBtn);
        btn_menuItemAdd->setObjectName(QString::fromUtf8("btn_menuItemAdd"));
        btn_menuItemAdd->setIcon(icon34);
        btn_menuItemAdd->setIconSize(QSize(32, 32));

        horizontalLayout_16->addWidget(btn_menuItemAdd);

        btn_menuItemEdit = new QPushButton(f_menuItemDbBtn);
        btn_menuItemEdit->setObjectName(QString::fromUtf8("btn_menuItemEdit"));
        btn_menuItemEdit->setEnabled(false);
        btn_menuItemEdit->setIcon(icon35);
        btn_menuItemEdit->setIconSize(QSize(32, 32));

        horizontalLayout_16->addWidget(btn_menuItemEdit);

        btn_menuItemDelete = new QPushButton(f_menuItemDbBtn);
        btn_menuItemDelete->setObjectName(QString::fromUtf8("btn_menuItemDelete"));
        btn_menuItemDelete->setEnabled(false);
        btn_menuItemDelete->setIcon(icon20);
        btn_menuItemDelete->setIconSize(QSize(32, 32));

        horizontalLayout_16->addWidget(btn_menuItemDelete);

        btn_menuItemClear = new QPushButton(f_menuItemDbBtn);
        btn_menuItemClear->setObjectName(QString::fromUtf8("btn_menuItemClear"));
        btn_menuItemClear->setEnabled(true);
        btn_menuItemClear->setIcon(icon21);
        btn_menuItemClear->setIconSize(QSize(32, 32));

        horizontalLayout_16->addWidget(btn_menuItemClear);


        verticalLayout_18->addWidget(f_menuItemDbBtn);


        horizontalLayout_8->addWidget(f_menuItemInputs);

        f_menuItemDb = new QFrame(tab_menu);
        f_menuItemDb->setObjectName(QString::fromUtf8("f_menuItemDb"));
        sizePolicy3.setHeightForWidth(f_menuItemDb->sizePolicy().hasHeightForWidth());
        f_menuItemDb->setSizePolicy(sizePolicy3);
        f_menuItemDb->setFrameShape(QFrame::StyledPanel);
        f_menuItemDb->setFrameShadow(QFrame::Raised);
        verticalLayout_17 = new QVBoxLayout(f_menuItemDb);
        verticalLayout_17->setObjectName(QString::fromUtf8("verticalLayout_17"));
        tw_menuItem = new QTableWidget(f_menuItemDb);
        tw_menuItem->setObjectName(QString::fromUtf8("tw_menuItem"));
        tw_menuItem->setFont(font8);
        tw_menuItem->setEditTriggers(QAbstractItemView::NoEditTriggers);
        tw_menuItem->setSelectionMode(QAbstractItemView::SingleSelection);
        tw_menuItem->setSelectionBehavior(QAbstractItemView::SelectRows);
        tw_menuItem->horizontalHeader()->setProperty("showSortIndicator", QVariant(true));
        tw_menuItem->verticalHeader()->setCascadingSectionResizes(true);
        tw_menuItem->verticalHeader()->setProperty("showSortIndicator", QVariant(false));

        verticalLayout_17->addWidget(tw_menuItem);


        horizontalLayout_8->addWidget(f_menuItemDb);

        QIcon icon40;
        icon40.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-hamburger.svg"), QSize(), QIcon::Normal, QIcon::Off);
        tw_database->addTab(tab_menu, icon40, QString());
        tab = new QWidget();
        tab->setObjectName(QString::fromUtf8("tab"));
        gridLayout_19 = new QGridLayout(tab);
        gridLayout_19->setObjectName(QString::fromUtf8("gridLayout_19"));
        f_menuCategoryCustomDb = new QFrame(tab);
        f_menuCategoryCustomDb->setObjectName(QString::fromUtf8("f_menuCategoryCustomDb"));
        f_menuCategoryCustomDb->setFrameShape(QFrame::StyledPanel);
        f_menuCategoryCustomDb->setFrameShadow(QFrame::Raised);
        verticalLayout_77 = new QVBoxLayout(f_menuCategoryCustomDb);
        verticalLayout_77->setObjectName(QString::fromUtf8("verticalLayout_77"));
        tw_menuCategoryCustom = new QTableWidget(f_menuCategoryCustomDb);
        tw_menuCategoryCustom->setObjectName(QString::fromUtf8("tw_menuCategoryCustom"));
        tw_menuCategoryCustom->setFont(font8);
        tw_menuCategoryCustom->setEditTriggers(QAbstractItemView::NoEditTriggers);
        tw_menuCategoryCustom->setSelectionMode(QAbstractItemView::SingleSelection);
        tw_menuCategoryCustom->setSelectionBehavior(QAbstractItemView::SelectRows);
        tw_menuCategoryCustom->horizontalHeader()->setProperty("showSortIndicator", QVariant(true));
        tw_menuCategoryCustom->verticalHeader()->setCascadingSectionResizes(true);
        tw_menuCategoryCustom->verticalHeader()->setProperty("showSortIndicator", QVariant(false));

        verticalLayout_77->addWidget(tw_menuCategoryCustom);


        gridLayout_19->addWidget(f_menuCategoryCustomDb, 0, 1, 1, 1);

        f_menuCategoryCustom = new QFrame(tab);
        f_menuCategoryCustom->setObjectName(QString::fromUtf8("f_menuCategoryCustom"));
        f_menuCategoryCustom->setStyleSheet(QString::fromUtf8("QFrame\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	\n"
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
"\n"
"\n"
"QComboBox\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}"));
        f_menuCategoryCustom->setFrameShape(QFrame::StyledPanel);
        f_menuCategoryCustom->setFrameShadow(QFrame::Raised);
        verticalLayout_75 = new QVBoxLayout(f_menuCategoryCustom);
        verticalLayout_75->setObjectName(QString::fromUtf8("verticalLayout_75"));
        gb_menuCategoryCustom = new QGroupBox(f_menuCategoryCustom);
        gb_menuCategoryCustom->setObjectName(QString::fromUtf8("gb_menuCategoryCustom"));
        gb_menuCategoryCustom->setFont(font5);
        gb_menuCategoryCustom->setStyleSheet(QString::fromUtf8(""));
        gb_menuCategoryCustom->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);
        verticalLayout_76 = new QVBoxLayout(gb_menuCategoryCustom);
        verticalLayout_76->setObjectName(QString::fromUtf8("verticalLayout_76"));
        le_menuCategoryCustomName = new QLineEdit(gb_menuCategoryCustom);
        le_menuCategoryCustomName->setObjectName(QString::fromUtf8("le_menuCategoryCustomName"));
        le_menuCategoryCustomName->setMaxLength(40);
        le_menuCategoryCustomName->setClearButtonEnabled(true);

        verticalLayout_76->addWidget(le_menuCategoryCustomName);

        cb_menuCategoryCustomPrinting = new QComboBox(gb_menuCategoryCustom);
        cb_menuCategoryCustomPrinting->addItem(QString());
        cb_menuCategoryCustomPrinting->addItem(QString());
        cb_menuCategoryCustomPrinting->addItem(QString());
        cb_menuCategoryCustomPrinting->setObjectName(QString::fromUtf8("cb_menuCategoryCustomPrinting"));

        verticalLayout_76->addWidget(cb_menuCategoryCustomPrinting);


        verticalLayout_75->addWidget(gb_menuCategoryCustom);

        f_menuCategoryCustomDbBtn = new QFrame(f_menuCategoryCustom);
        f_menuCategoryCustomDbBtn->setObjectName(QString::fromUtf8("f_menuCategoryCustomDbBtn"));
        sizePolicy1.setHeightForWidth(f_menuCategoryCustomDbBtn->sizePolicy().hasHeightForWidth());
        f_menuCategoryCustomDbBtn->setSizePolicy(sizePolicy1);
        f_menuCategoryCustomDbBtn->setFrameShape(QFrame::StyledPanel);
        f_menuCategoryCustomDbBtn->setFrameShadow(QFrame::Raised);
        horizontalLayout_54 = new QHBoxLayout(f_menuCategoryCustomDbBtn);
        horizontalLayout_54->setSpacing(5);
        horizontalLayout_54->setObjectName(QString::fromUtf8("horizontalLayout_54"));
        horizontalLayout_54->setContentsMargins(0, 0, 0, 0);
        btn_menuCategoryCustomAdd = new QPushButton(f_menuCategoryCustomDbBtn);
        btn_menuCategoryCustomAdd->setObjectName(QString::fromUtf8("btn_menuCategoryCustomAdd"));
        btn_menuCategoryCustomAdd->setIcon(icon34);
        btn_menuCategoryCustomAdd->setIconSize(QSize(32, 32));

        horizontalLayout_54->addWidget(btn_menuCategoryCustomAdd);

        btn_menuCategoryCustomEdit = new QPushButton(f_menuCategoryCustomDbBtn);
        btn_menuCategoryCustomEdit->setObjectName(QString::fromUtf8("btn_menuCategoryCustomEdit"));
        btn_menuCategoryCustomEdit->setEnabled(false);
        btn_menuCategoryCustomEdit->setIcon(icon35);
        btn_menuCategoryCustomEdit->setIconSize(QSize(32, 32));

        horizontalLayout_54->addWidget(btn_menuCategoryCustomEdit);

        btn_menuCategoryCustomDelete = new QPushButton(f_menuCategoryCustomDbBtn);
        btn_menuCategoryCustomDelete->setObjectName(QString::fromUtf8("btn_menuCategoryCustomDelete"));
        btn_menuCategoryCustomDelete->setEnabled(false);
        btn_menuCategoryCustomDelete->setIcon(icon20);
        btn_menuCategoryCustomDelete->setIconSize(QSize(32, 32));

        horizontalLayout_54->addWidget(btn_menuCategoryCustomDelete);

        btn_menuCategoryCustomClear = new QPushButton(f_menuCategoryCustomDbBtn);
        btn_menuCategoryCustomClear->setObjectName(QString::fromUtf8("btn_menuCategoryCustomClear"));
        btn_menuCategoryCustomClear->setEnabled(true);
        btn_menuCategoryCustomClear->setIcon(icon21);
        btn_menuCategoryCustomClear->setIconSize(QSize(32, 32));

        horizontalLayout_54->addWidget(btn_menuCategoryCustomClear);


        verticalLayout_75->addWidget(f_menuCategoryCustomDbBtn);


        gridLayout_19->addWidget(f_menuCategoryCustom, 0, 0, 1, 1);

        QIcon icon41;
        icon41.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-book-alt.svg"), QSize(), QIcon::Normal, QIcon::Off);
        tw_database->addTab(tab, icon41, QString());
        tab_supplement = new QWidget();
        tab_supplement->setObjectName(QString::fromUtf8("tab_supplement"));
        horizontalLayout_49 = new QHBoxLayout(tab_supplement);
        horizontalLayout_49->setObjectName(QString::fromUtf8("horizontalLayout_49"));
        f_supplementInputs = new QFrame(tab_supplement);
        f_supplementInputs->setObjectName(QString::fromUtf8("f_supplementInputs"));
        f_supplementInputs->setStyleSheet(QString::fromUtf8("QFrame\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	\n"
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
"}"));
        f_supplementInputs->setFrameShape(QFrame::StyledPanel);
        f_supplementInputs->setFrameShadow(QFrame::Raised);
        verticalLayout_66 = new QVBoxLayout(f_supplementInputs);
        verticalLayout_66->setObjectName(QString::fromUtf8("verticalLayout_66"));
        gb_supplement = new QGroupBox(f_supplementInputs);
        gb_supplement->setObjectName(QString::fromUtf8("gb_supplement"));
        gb_supplement->setFont(font3);
        gb_supplement->setStyleSheet(QString::fromUtf8("QLineEdit\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
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
""));
        verticalLayout_70 = new QVBoxLayout(gb_supplement);
        verticalLayout_70->setObjectName(QString::fromUtf8("verticalLayout_70"));
        le_supplementName = new QLineEdit(gb_supplement);
        le_supplementName->setObjectName(QString::fromUtf8("le_supplementName"));
        le_supplementName->setMaxLength(150);
        le_supplementName->setClearButtonEnabled(true);

        verticalLayout_70->addWidget(le_supplementName);

        cb_supplementProduct = new QComboBox(gb_supplement);
        cb_supplementProduct->setObjectName(QString::fromUtf8("cb_supplementProduct"));

        verticalLayout_70->addWidget(cb_supplementProduct);

        le_supplementQuantity = new QLineEdit(gb_supplement);
        le_supplementQuantity->setObjectName(QString::fromUtf8("le_supplementQuantity"));
        le_supplementQuantity->setMaxLength(20);
        le_supplementQuantity->setClearButtonEnabled(true);

        verticalLayout_70->addWidget(le_supplementQuantity);

        le_supplementPrice = new QLineEdit(gb_supplement);
        le_supplementPrice->setObjectName(QString::fromUtf8("le_supplementPrice"));
        le_supplementPrice->setMaxLength(20);
        le_supplementPrice->setClearButtonEnabled(true);

        verticalLayout_70->addWidget(le_supplementPrice);


        verticalLayout_66->addWidget(gb_supplement);

        f_expenseDbBtn_4 = new QFrame(f_supplementInputs);
        f_expenseDbBtn_4->setObjectName(QString::fromUtf8("f_expenseDbBtn_4"));
        sizePolicy1.setHeightForWidth(f_expenseDbBtn_4->sizePolicy().hasHeightForWidth());
        f_expenseDbBtn_4->setSizePolicy(sizePolicy1);
        f_expenseDbBtn_4->setFrameShape(QFrame::StyledPanel);
        f_expenseDbBtn_4->setFrameShadow(QFrame::Raised);
        horizontalLayout_48 = new QHBoxLayout(f_expenseDbBtn_4);
        horizontalLayout_48->setSpacing(5);
        horizontalLayout_48->setObjectName(QString::fromUtf8("horizontalLayout_48"));
        horizontalLayout_48->setContentsMargins(0, 0, 0, 0);
        btn_supplementAdd = new QPushButton(f_expenseDbBtn_4);
        btn_supplementAdd->setObjectName(QString::fromUtf8("btn_supplementAdd"));
        btn_supplementAdd->setIcon(icon34);
        btn_supplementAdd->setIconSize(QSize(32, 32));

        horizontalLayout_48->addWidget(btn_supplementAdd);

        btn_supplementEdit = new QPushButton(f_expenseDbBtn_4);
        btn_supplementEdit->setObjectName(QString::fromUtf8("btn_supplementEdit"));
        btn_supplementEdit->setEnabled(false);
        btn_supplementEdit->setIcon(icon35);
        btn_supplementEdit->setIconSize(QSize(32, 32));

        horizontalLayout_48->addWidget(btn_supplementEdit);

        btn_supplementDelete = new QPushButton(f_expenseDbBtn_4);
        btn_supplementDelete->setObjectName(QString::fromUtf8("btn_supplementDelete"));
        btn_supplementDelete->setEnabled(false);
        btn_supplementDelete->setIcon(icon20);
        btn_supplementDelete->setIconSize(QSize(32, 32));

        horizontalLayout_48->addWidget(btn_supplementDelete);

        btn_supplementClear = new QPushButton(f_expenseDbBtn_4);
        btn_supplementClear->setObjectName(QString::fromUtf8("btn_supplementClear"));
        btn_supplementClear->setEnabled(true);
        btn_supplementClear->setIcon(icon21);
        btn_supplementClear->setIconSize(QSize(32, 32));

        horizontalLayout_48->addWidget(btn_supplementClear);


        verticalLayout_66->addWidget(f_expenseDbBtn_4);


        horizontalLayout_49->addWidget(f_supplementInputs);

        f_supplementDb = new QFrame(tab_supplement);
        f_supplementDb->setObjectName(QString::fromUtf8("f_supplementDb"));
        f_supplementDb->setFrameShape(QFrame::StyledPanel);
        f_supplementDb->setFrameShadow(QFrame::Raised);
        verticalLayout_65 = new QVBoxLayout(f_supplementDb);
        verticalLayout_65->setObjectName(QString::fromUtf8("verticalLayout_65"));
        tw_supplement = new QTableWidget(f_supplementDb);
        tw_supplement->setObjectName(QString::fromUtf8("tw_supplement"));
        tw_supplement->setFont(font7);
        tw_supplement->setEditTriggers(QAbstractItemView::NoEditTriggers);
        tw_supplement->setSelectionMode(QAbstractItemView::SingleSelection);
        tw_supplement->setSelectionBehavior(QAbstractItemView::SelectRows);
        tw_supplement->horizontalHeader()->setProperty("showSortIndicator", QVariant(true));
        tw_supplement->verticalHeader()->setCascadingSectionResizes(true);
        tw_supplement->verticalHeader()->setProperty("showSortIndicator", QVariant(false));

        verticalLayout_65->addWidget(tw_supplement);


        horizontalLayout_49->addWidget(f_supplementDb);

        QIcon icon42;
        icon42.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-confetti.svg"), QSize(), QIcon::Normal, QIcon::Off);
        tw_database->addTab(tab_supplement, icon42, QString());
        tab_expense = new QWidget();
        tab_expense->setObjectName(QString::fromUtf8("tab_expense"));
        horizontalLayout_9 = new QHBoxLayout(tab_expense);
        horizontalLayout_9->setObjectName(QString::fromUtf8("horizontalLayout_9"));
        f_expenseInputs = new QFrame(tab_expense);
        f_expenseInputs->setObjectName(QString::fromUtf8("f_expenseInputs"));
        f_expenseInputs->setStyleSheet(QString::fromUtf8("QFrame\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	\n"
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
"}"));
        f_expenseInputs->setFrameShape(QFrame::StyledPanel);
        f_expenseInputs->setFrameShadow(QFrame::Raised);
        verticalLayout_20 = new QVBoxLayout(f_expenseInputs);
        verticalLayout_20->setObjectName(QString::fromUtf8("verticalLayout_20"));
        gb_expense = new QGroupBox(f_expenseInputs);
        gb_expense->setObjectName(QString::fromUtf8("gb_expense"));
        gb_expense->setFont(font5);
        gb_expense->setStyleSheet(QString::fromUtf8("QLineEdit\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
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
""));
        verticalLayout_21 = new QVBoxLayout(gb_expense);
        verticalLayout_21->setObjectName(QString::fromUtf8("verticalLayout_21"));
        le_expenseName = new QLineEdit(gb_expense);
        le_expenseName->setObjectName(QString::fromUtf8("le_expenseName"));
        le_expenseName->setMaxLength(40);
        le_expenseName->setClearButtonEnabled(true);

        verticalLayout_21->addWidget(le_expenseName);

        cb_expenseCategory = new QComboBox(gb_expense);
        cb_expenseCategory->setObjectName(QString::fromUtf8("cb_expenseCategory"));

        verticalLayout_21->addWidget(cb_expenseCategory);

        le_expenseUnit = new QLineEdit(gb_expense);
        le_expenseUnit->setObjectName(QString::fromUtf8("le_expenseUnit"));
        le_expenseUnit->setMaxLength(20);
        le_expenseUnit->setClearButtonEnabled(true);

        verticalLayout_21->addWidget(le_expenseUnit);

        le_expenseQuantity = new QLineEdit(gb_expense);
        le_expenseQuantity->setObjectName(QString::fromUtf8("le_expenseQuantity"));
        le_expenseQuantity->setMaxLength(20);
        le_expenseQuantity->setClearButtonEnabled(true);

        verticalLayout_21->addWidget(le_expenseQuantity);

        le_expensePrice = new QLineEdit(gb_expense);
        le_expensePrice->setObjectName(QString::fromUtf8("le_expensePrice"));
        le_expensePrice->setMaxLength(20);
        le_expensePrice->setClearButtonEnabled(true);

        verticalLayout_21->addWidget(le_expensePrice);

        cb_expenseSupplier = new QComboBox(gb_expense);
        cb_expenseSupplier->addItem(QString());
        cb_expenseSupplier->setObjectName(QString::fromUtf8("cb_expenseSupplier"));

        verticalLayout_21->addWidget(cb_expenseSupplier);

        cb_expensePayed = new QCheckBox(gb_expense);
        cb_expensePayed->setObjectName(QString::fromUtf8("cb_expensePayed"));
        cb_expensePayed->setFont(font3);
        cb_expensePayed->setLayoutDirection(Qt::LeftToRight);
        cb_expensePayed->setIcon(icon27);
        cb_expensePayed->setIconSize(QSize(32, 32));
        cb_expensePayed->setChecked(true);

        verticalLayout_21->addWidget(cb_expensePayed);


        verticalLayout_20->addWidget(gb_expense);

        f_expenseDbBtn = new QFrame(f_expenseInputs);
        f_expenseDbBtn->setObjectName(QString::fromUtf8("f_expenseDbBtn"));
        sizePolicy1.setHeightForWidth(f_expenseDbBtn->sizePolicy().hasHeightForWidth());
        f_expenseDbBtn->setSizePolicy(sizePolicy1);
        f_expenseDbBtn->setFrameShape(QFrame::StyledPanel);
        f_expenseDbBtn->setFrameShadow(QFrame::Raised);
        horizontalLayout_18 = new QHBoxLayout(f_expenseDbBtn);
        horizontalLayout_18->setSpacing(5);
        horizontalLayout_18->setObjectName(QString::fromUtf8("horizontalLayout_18"));
        horizontalLayout_18->setContentsMargins(0, 0, 0, 0);
        btn_expenseAdd = new QPushButton(f_expenseDbBtn);
        btn_expenseAdd->setObjectName(QString::fromUtf8("btn_expenseAdd"));
        btn_expenseAdd->setIcon(icon34);
        btn_expenseAdd->setIconSize(QSize(32, 32));

        horizontalLayout_18->addWidget(btn_expenseAdd);

        btn_expenseEdit = new QPushButton(f_expenseDbBtn);
        btn_expenseEdit->setObjectName(QString::fromUtf8("btn_expenseEdit"));
        btn_expenseEdit->setEnabled(false);
        btn_expenseEdit->setIcon(icon35);
        btn_expenseEdit->setIconSize(QSize(32, 32));

        horizontalLayout_18->addWidget(btn_expenseEdit);

        btn_expenseDelete = new QPushButton(f_expenseDbBtn);
        btn_expenseDelete->setObjectName(QString::fromUtf8("btn_expenseDelete"));
        btn_expenseDelete->setEnabled(false);
        btn_expenseDelete->setIcon(icon20);
        btn_expenseDelete->setIconSize(QSize(32, 32));

        horizontalLayout_18->addWidget(btn_expenseDelete);

        btn_expenseClear = new QPushButton(f_expenseDbBtn);
        btn_expenseClear->setObjectName(QString::fromUtf8("btn_expenseClear"));
        btn_expenseClear->setEnabled(true);
        btn_expenseClear->setIcon(icon21);
        btn_expenseClear->setIconSize(QSize(32, 32));

        horizontalLayout_18->addWidget(btn_expenseClear);


        verticalLayout_20->addWidget(f_expenseDbBtn);


        horizontalLayout_9->addWidget(f_expenseInputs);

        f_expenseDb = new QFrame(tab_expense);
        f_expenseDb->setObjectName(QString::fromUtf8("f_expenseDb"));
        f_expenseDb->setFrameShape(QFrame::StyledPanel);
        f_expenseDb->setFrameShadow(QFrame::Raised);
        verticalLayout_22 = new QVBoxLayout(f_expenseDb);
        verticalLayout_22->setObjectName(QString::fromUtf8("verticalLayout_22"));
        tw_expense = new QTableWidget(f_expenseDb);
        tw_expense->setObjectName(QString::fromUtf8("tw_expense"));
        tw_expense->setFont(font8);
        tw_expense->setEditTriggers(QAbstractItemView::NoEditTriggers);
        tw_expense->setSelectionMode(QAbstractItemView::SingleSelection);
        tw_expense->setSelectionBehavior(QAbstractItemView::SelectRows);
        tw_expense->horizontalHeader()->setProperty("showSortIndicator", QVariant(true));
        tw_expense->verticalHeader()->setCascadingSectionResizes(true);
        tw_expense->verticalHeader()->setProperty("showSortIndicator", QVariant(false));

        verticalLayout_22->addWidget(tw_expense);


        horizontalLayout_9->addWidget(f_expenseDb);

        QIcon icon43;
        icon43.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-shopping-cart-add.svg"), QSize(), QIcon::Normal, QIcon::Off);
        tw_database->addTab(tab_expense, icon43, QString());
        tab_expenseCategory = new QWidget();
        tab_expenseCategory->setObjectName(QString::fromUtf8("tab_expenseCategory"));
        horizontalLayout_42 = new QHBoxLayout(tab_expenseCategory);
        horizontalLayout_42->setObjectName(QString::fromUtf8("horizontalLayout_42"));
        f_expenseCategoryInputs = new QFrame(tab_expenseCategory);
        f_expenseCategoryInputs->setObjectName(QString::fromUtf8("f_expenseCategoryInputs"));
        f_expenseCategoryInputs->setStyleSheet(QString::fromUtf8("QFrame\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	\n"
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
"}"));
        f_expenseCategoryInputs->setFrameShape(QFrame::StyledPanel);
        f_expenseCategoryInputs->setFrameShadow(QFrame::Raised);
        verticalLayout_52 = new QVBoxLayout(f_expenseCategoryInputs);
        verticalLayout_52->setObjectName(QString::fromUtf8("verticalLayout_52"));
        gb_expenseCategory = new QGroupBox(f_expenseCategoryInputs);
        gb_expenseCategory->setObjectName(QString::fromUtf8("gb_expenseCategory"));
        gb_expenseCategory->setFont(font5);
        gb_expenseCategory->setStyleSheet(QString::fromUtf8("QLineEdit\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
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
"QCheckBox\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
""));
        gb_expenseCategory->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);
        verticalLayout_53 = new QVBoxLayout(gb_expenseCategory);
        verticalLayout_53->setObjectName(QString::fromUtf8("verticalLayout_53"));
        le_expenseCategoryName = new QLineEdit(gb_expenseCategory);
        le_expenseCategoryName->setObjectName(QString::fromUtf8("le_expenseCategoryName"));
        le_expenseCategoryName->setMaxLength(40);
        le_expenseCategoryName->setClearButtonEnabled(true);

        verticalLayout_53->addWidget(le_expenseCategoryName);

        cb_expenseCategorySaveToStock = new QCheckBox(gb_expenseCategory);
        cb_expenseCategorySaveToStock->setObjectName(QString::fromUtf8("cb_expenseCategorySaveToStock"));
        cb_expenseCategorySaveToStock->setFont(font3);
        cb_expenseCategorySaveToStock->setLayoutDirection(Qt::LeftToRight);
        QIcon icon44;
        icon44.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-cursor-plus.svg"), QSize(), QIcon::Normal, QIcon::Off);
        cb_expenseCategorySaveToStock->setIcon(icon44);
        cb_expenseCategorySaveToStock->setIconSize(QSize(32, 32));
        cb_expenseCategorySaveToStock->setChecked(true);

        verticalLayout_53->addWidget(cb_expenseCategorySaveToStock);

        cb_expenseCategoryIsIngredient = new QCheckBox(gb_expenseCategory);
        cb_expenseCategoryIsIngredient->setObjectName(QString::fromUtf8("cb_expenseCategoryIsIngredient"));
        cb_expenseCategoryIsIngredient->setFont(font3);
        cb_expenseCategoryIsIngredient->setLayoutDirection(Qt::LeftToRight);
        cb_expenseCategoryIsIngredient->setIcon(icon44);
        cb_expenseCategoryIsIngredient->setIconSize(QSize(32, 32));
        cb_expenseCategoryIsIngredient->setChecked(true);

        verticalLayout_53->addWidget(cb_expenseCategoryIsIngredient);


        verticalLayout_52->addWidget(gb_expenseCategory);

        f_expenseCategoryDbBtn = new QFrame(f_expenseCategoryInputs);
        f_expenseCategoryDbBtn->setObjectName(QString::fromUtf8("f_expenseCategoryDbBtn"));
        sizePolicy1.setHeightForWidth(f_expenseCategoryDbBtn->sizePolicy().hasHeightForWidth());
        f_expenseCategoryDbBtn->setSizePolicy(sizePolicy1);
        f_expenseCategoryDbBtn->setFrameShape(QFrame::StyledPanel);
        f_expenseCategoryDbBtn->setFrameShadow(QFrame::Raised);
        horizontalLayout_41 = new QHBoxLayout(f_expenseCategoryDbBtn);
        horizontalLayout_41->setSpacing(5);
        horizontalLayout_41->setObjectName(QString::fromUtf8("horizontalLayout_41"));
        horizontalLayout_41->setContentsMargins(0, 0, 0, 0);
        btn_expenseCategoryAdd = new QPushButton(f_expenseCategoryDbBtn);
        btn_expenseCategoryAdd->setObjectName(QString::fromUtf8("btn_expenseCategoryAdd"));
        btn_expenseCategoryAdd->setIcon(icon34);
        btn_expenseCategoryAdd->setIconSize(QSize(32, 32));

        horizontalLayout_41->addWidget(btn_expenseCategoryAdd);

        btn_expenseCategoryEdit = new QPushButton(f_expenseCategoryDbBtn);
        btn_expenseCategoryEdit->setObjectName(QString::fromUtf8("btn_expenseCategoryEdit"));
        btn_expenseCategoryEdit->setEnabled(false);
        btn_expenseCategoryEdit->setIcon(icon35);
        btn_expenseCategoryEdit->setIconSize(QSize(32, 32));

        horizontalLayout_41->addWidget(btn_expenseCategoryEdit);

        btn_expenseCategoryDelete = new QPushButton(f_expenseCategoryDbBtn);
        btn_expenseCategoryDelete->setObjectName(QString::fromUtf8("btn_expenseCategoryDelete"));
        btn_expenseCategoryDelete->setEnabled(false);
        btn_expenseCategoryDelete->setIcon(icon20);
        btn_expenseCategoryDelete->setIconSize(QSize(32, 32));

        horizontalLayout_41->addWidget(btn_expenseCategoryDelete);

        btn_expenseCategoryClear = new QPushButton(f_expenseCategoryDbBtn);
        btn_expenseCategoryClear->setObjectName(QString::fromUtf8("btn_expenseCategoryClear"));
        btn_expenseCategoryClear->setEnabled(true);
        btn_expenseCategoryClear->setIcon(icon21);
        btn_expenseCategoryClear->setIconSize(QSize(32, 32));

        horizontalLayout_41->addWidget(btn_expenseCategoryClear);


        verticalLayout_52->addWidget(f_expenseCategoryDbBtn);


        horizontalLayout_42->addWidget(f_expenseCategoryInputs);

        f_expenseCategoryDb = new QFrame(tab_expenseCategory);
        f_expenseCategoryDb->setObjectName(QString::fromUtf8("f_expenseCategoryDb"));
        f_expenseCategoryDb->setFrameShape(QFrame::StyledPanel);
        f_expenseCategoryDb->setFrameShadow(QFrame::Raised);
        verticalLayout_51 = new QVBoxLayout(f_expenseCategoryDb);
        verticalLayout_51->setObjectName(QString::fromUtf8("verticalLayout_51"));
        tw_expenseCategory = new QTableWidget(f_expenseCategoryDb);
        tw_expenseCategory->setObjectName(QString::fromUtf8("tw_expenseCategory"));
        tw_expenseCategory->setFont(font8);
        tw_expenseCategory->setEditTriggers(QAbstractItemView::NoEditTriggers);
        tw_expenseCategory->setSelectionMode(QAbstractItemView::SingleSelection);
        tw_expenseCategory->setSelectionBehavior(QAbstractItemView::SelectRows);
        tw_expenseCategory->horizontalHeader()->setProperty("showSortIndicator", QVariant(true));
        tw_expenseCategory->verticalHeader()->setCascadingSectionResizes(true);
        tw_expenseCategory->verticalHeader()->setProperty("showSortIndicator", QVariant(false));

        verticalLayout_51->addWidget(tw_expenseCategory);


        horizontalLayout_42->addWidget(f_expenseCategoryDb);

        QIcon icon45;
        icon45.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-shopping-cart-check.svg"), QSize(), QIcon::Normal, QIcon::Off);
        tw_database->addTab(tab_expenseCategory, icon45, QString());
        tab_supplier = new QWidget();
        tab_supplier->setObjectName(QString::fromUtf8("tab_supplier"));
        horizontalLayout_47 = new QHBoxLayout(tab_supplier);
        horizontalLayout_47->setObjectName(QString::fromUtf8("horizontalLayout_47"));
        f_supplierInputs = new QFrame(tab_supplier);
        f_supplierInputs->setObjectName(QString::fromUtf8("f_supplierInputs"));
        f_supplierInputs->setStyleSheet(QString::fromUtf8("QFrame\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	\n"
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
"}"));
        f_supplierInputs->setFrameShape(QFrame::StyledPanel);
        f_supplierInputs->setFrameShadow(QFrame::Raised);
        verticalLayout_56 = new QVBoxLayout(f_supplierInputs);
        verticalLayout_56->setObjectName(QString::fromUtf8("verticalLayout_56"));
        gb_supplier = new QGroupBox(f_supplierInputs);
        gb_supplier->setObjectName(QString::fromUtf8("gb_supplier"));
        gb_supplier->setFont(font3);
        gb_supplier->setStyleSheet(QString::fromUtf8("QLineEdit\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
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
""));
        verticalLayout_64 = new QVBoxLayout(gb_supplier);
        verticalLayout_64->setObjectName(QString::fromUtf8("verticalLayout_64"));
        le_supplierName = new QLineEdit(gb_supplier);
        le_supplierName->setObjectName(QString::fromUtf8("le_supplierName"));
        le_supplierName->setMaxLength(150);
        le_supplierName->setClearButtonEnabled(true);

        verticalLayout_64->addWidget(le_supplierName);

        le_supplierPhone = new QLineEdit(gb_supplier);
        le_supplierPhone->setObjectName(QString::fromUtf8("le_supplierPhone"));
        le_supplierPhone->setMaxLength(20);
        le_supplierPhone->setClearButtonEnabled(true);

        verticalLayout_64->addWidget(le_supplierPhone);

        le_supplierAddress = new QLineEdit(gb_supplier);
        le_supplierAddress->setObjectName(QString::fromUtf8("le_supplierAddress"));
        le_supplierAddress->setMaxLength(250);
        le_supplierAddress->setClearButtonEnabled(true);

        verticalLayout_64->addWidget(le_supplierAddress);

        le_supplierMail = new QLineEdit(gb_supplier);
        le_supplierMail->setObjectName(QString::fromUtf8("le_supplierMail"));
        le_supplierMail->setMaxLength(20);
        le_supplierMail->setClearButtonEnabled(true);

        verticalLayout_64->addWidget(le_supplierMail);


        verticalLayout_56->addWidget(gb_supplier);

        f_expenseDbBtn_3 = new QFrame(f_supplierInputs);
        f_expenseDbBtn_3->setObjectName(QString::fromUtf8("f_expenseDbBtn_3"));
        sizePolicy1.setHeightForWidth(f_expenseDbBtn_3->sizePolicy().hasHeightForWidth());
        f_expenseDbBtn_3->setSizePolicy(sizePolicy1);
        f_expenseDbBtn_3->setFrameShape(QFrame::StyledPanel);
        f_expenseDbBtn_3->setFrameShadow(QFrame::Raised);
        horizontalLayout_43 = new QHBoxLayout(f_expenseDbBtn_3);
        horizontalLayout_43->setSpacing(5);
        horizontalLayout_43->setObjectName(QString::fromUtf8("horizontalLayout_43"));
        horizontalLayout_43->setContentsMargins(0, 0, 0, 0);
        btn_supplierAdd = new QPushButton(f_expenseDbBtn_3);
        btn_supplierAdd->setObjectName(QString::fromUtf8("btn_supplierAdd"));
        btn_supplierAdd->setIcon(icon34);
        btn_supplierAdd->setIconSize(QSize(32, 32));

        horizontalLayout_43->addWidget(btn_supplierAdd);

        btn_supplierEdit = new QPushButton(f_expenseDbBtn_3);
        btn_supplierEdit->setObjectName(QString::fromUtf8("btn_supplierEdit"));
        btn_supplierEdit->setEnabled(false);
        btn_supplierEdit->setIcon(icon35);
        btn_supplierEdit->setIconSize(QSize(32, 32));

        horizontalLayout_43->addWidget(btn_supplierEdit);

        btn_supplierDelete = new QPushButton(f_expenseDbBtn_3);
        btn_supplierDelete->setObjectName(QString::fromUtf8("btn_supplierDelete"));
        btn_supplierDelete->setEnabled(false);
        btn_supplierDelete->setIcon(icon20);
        btn_supplierDelete->setIconSize(QSize(32, 32));

        horizontalLayout_43->addWidget(btn_supplierDelete);

        btn_supplierClear = new QPushButton(f_expenseDbBtn_3);
        btn_supplierClear->setObjectName(QString::fromUtf8("btn_supplierClear"));
        btn_supplierClear->setEnabled(true);
        btn_supplierClear->setIcon(icon21);
        btn_supplierClear->setIconSize(QSize(32, 32));

        horizontalLayout_43->addWidget(btn_supplierClear);


        verticalLayout_56->addWidget(f_expenseDbBtn_3);


        horizontalLayout_47->addWidget(f_supplierInputs);

        f_supplierDb = new QFrame(tab_supplier);
        f_supplierDb->setObjectName(QString::fromUtf8("f_supplierDb"));
        f_supplierDb->setFrameShape(QFrame::StyledPanel);
        f_supplierDb->setFrameShadow(QFrame::Raised);
        verticalLayout_55 = new QVBoxLayout(f_supplierDb);
        verticalLayout_55->setObjectName(QString::fromUtf8("verticalLayout_55"));
        tw_supplier = new QTableWidget(f_supplierDb);
        tw_supplier->setObjectName(QString::fromUtf8("tw_supplier"));
        tw_supplier->setFont(font7);
        tw_supplier->setEditTriggers(QAbstractItemView::NoEditTriggers);
        tw_supplier->setSelectionMode(QAbstractItemView::SingleSelection);
        tw_supplier->setSelectionBehavior(QAbstractItemView::SelectRows);
        tw_supplier->horizontalHeader()->setProperty("showSortIndicator", QVariant(true));
        tw_supplier->verticalHeader()->setCascadingSectionResizes(true);
        tw_supplier->verticalHeader()->setProperty("showSortIndicator", QVariant(false));

        verticalLayout_55->addWidget(tw_supplier);


        horizontalLayout_47->addWidget(f_supplierDb);

        tw_database->addTab(tab_supplier, icon19, QString());
        tab_customer = new QWidget();
        tab_customer->setObjectName(QString::fromUtf8("tab_customer"));
        horizontalLayout_10 = new QHBoxLayout(tab_customer);
        horizontalLayout_10->setObjectName(QString::fromUtf8("horizontalLayout_10"));
        f_customerInput = new QFrame(tab_customer);
        f_customerInput->setObjectName(QString::fromUtf8("f_customerInput"));
        f_customerInput->setStyleSheet(QString::fromUtf8("QFrame\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	\n"
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
"}"));
        f_customerInput->setFrameShape(QFrame::StyledPanel);
        f_customerInput->setFrameShadow(QFrame::Raised);
        verticalLayout_40 = new QVBoxLayout(f_customerInput);
        verticalLayout_40->setObjectName(QString::fromUtf8("verticalLayout_40"));
        gb_customer = new QGroupBox(f_customerInput);
        gb_customer->setObjectName(QString::fromUtf8("gb_customer"));
        gb_customer->setFont(font5);
        gb_customer->setStyleSheet(QString::fromUtf8("QLineEdit\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
""));
        verticalLayout_24 = new QVBoxLayout(gb_customer);
        verticalLayout_24->setObjectName(QString::fromUtf8("verticalLayout_24"));
        f_customerPic = new QFrame(gb_customer);
        f_customerPic->setObjectName(QString::fromUtf8("f_customerPic"));
        sizePolicy12.setHeightForWidth(f_customerPic->sizePolicy().hasHeightForWidth());
        f_customerPic->setSizePolicy(sizePolicy12);
        f_customerPic->setMinimumSize(QSize(100, 100));
        f_customerPic->setMaximumSize(QSize(800, 300));
        f_customerPic->setLayoutDirection(Qt::LeftToRight);
        f_customerPic->setStyleSheet(QString::fromUtf8(""));
        f_customerPic->setFrameShape(QFrame::StyledPanel);
        f_customerPic->setFrameShadow(QFrame::Raised);
        horizontalLayout_27 = new QHBoxLayout(f_customerPic);
        horizontalLayout_27->setSpacing(0);
        horizontalLayout_27->setObjectName(QString::fromUtf8("horizontalLayout_27"));
        horizontalLayout_27->setSizeConstraint(QLayout::SetMinimumSize);
        horizontalLayout_27->setContentsMargins(0, 0, 0, 0);
        l_customerPicture = new QLabel(f_customerPic);
        l_customerPicture->setObjectName(QString::fromUtf8("l_customerPicture"));
        sizePolicy.setHeightForWidth(l_customerPicture->sizePolicy().hasHeightForWidth());
        l_customerPicture->setSizePolicy(sizePolicy);
        l_customerPicture->setMinimumSize(QSize(250, 200));
        l_customerPicture->setMaximumSize(QSize(300, 300));
        l_customerPicture->setBaseSize(QSize(200, 200));
        l_customerPicture->setFont(font14);
        l_customerPicture->setLayoutDirection(Qt::LeftToRight);
        l_customerPicture->setAutoFillBackground(false);
        l_customerPicture->setStyleSheet(QString::fromUtf8(""));
        l_customerPicture->setFrameShape(QFrame::Box);
        l_customerPicture->setFrameShadow(QFrame::Plain);
        l_customerPicture->setScaledContents(true);
        l_customerPicture->setAlignment(Qt::AlignCenter);
        l_customerPicture->setWordWrap(false);

        horizontalLayout_27->addWidget(l_customerPicture);

        f_customerSetting = new QFrame(f_customerPic);
        f_customerSetting->setObjectName(QString::fromUtf8("f_customerSetting"));
        f_customerSetting->setFrameShape(QFrame::StyledPanel);
        f_customerSetting->setFrameShadow(QFrame::Raised);
        verticalLayout_45 = new QVBoxLayout(f_customerSetting);
        verticalLayout_45->setObjectName(QString::fromUtf8("verticalLayout_45"));
        btn_customerPicture = new QPushButton(f_customerSetting);
        btn_customerPicture->setObjectName(QString::fromUtf8("btn_customerPicture"));
        sizePolicy12.setHeightForWidth(btn_customerPicture->sizePolicy().hasHeightForWidth());
        btn_customerPicture->setSizePolicy(sizePolicy12);
        btn_customerPicture->setIcon(icon39);
        btn_customerPicture->setIconSize(QSize(32, 32));

        verticalLayout_45->addWidget(btn_customerPicture);

        btn_customerPictureClear = new QPushButton(f_customerSetting);
        btn_customerPictureClear->setObjectName(QString::fromUtf8("btn_customerPictureClear"));
        sizePolicy12.setHeightForWidth(btn_customerPictureClear->sizePolicy().hasHeightForWidth());
        btn_customerPictureClear->setSizePolicy(sizePolicy12);
        btn_customerPictureClear->setIcon(icon21);
        btn_customerPictureClear->setIconSize(QSize(32, 32));

        verticalLayout_45->addWidget(btn_customerPictureClear);


        horizontalLayout_27->addWidget(f_customerSetting);


        verticalLayout_24->addWidget(f_customerPic);

        le_customerName = new QLineEdit(gb_customer);
        le_customerName->setObjectName(QString::fromUtf8("le_customerName"));
        le_customerName->setInputMethodHints(Qt::ImhHiddenText);
        le_customerName->setMaxLength(150);
        le_customerName->setClearButtonEnabled(true);

        verticalLayout_24->addWidget(le_customerName);

        le_customerPhone = new QLineEdit(gb_customer);
        le_customerPhone->setObjectName(QString::fromUtf8("le_customerPhone"));
        le_customerPhone->setInputMethodHints(Qt::ImhDigitsOnly|Qt::ImhFormattedNumbersOnly);
        le_customerPhone->setMaxLength(20);
        le_customerPhone->setClearButtonEnabled(true);

        verticalLayout_24->addWidget(le_customerPhone);

        le_customerAddress = new QLineEdit(gb_customer);
        le_customerAddress->setObjectName(QString::fromUtf8("le_customerAddress"));
        le_customerAddress->setMaxLength(250);
        le_customerAddress->setClearButtonEnabled(true);

        verticalLayout_24->addWidget(le_customerAddress);

        le_customerScore = new QLineEdit(gb_customer);
        le_customerScore->setObjectName(QString::fromUtf8("le_customerScore"));
        le_customerScore->setInputMethodHints(Qt::ImhDigitsOnly);
        le_customerScore->setMaxLength(32767);
        le_customerScore->setClearButtonEnabled(true);

        verticalLayout_24->addWidget(le_customerScore);


        verticalLayout_40->addWidget(gb_customer);

        f_customerDbBtn = new QFrame(f_customerInput);
        f_customerDbBtn->setObjectName(QString::fromUtf8("f_customerDbBtn"));
        sizePolicy1.setHeightForWidth(f_customerDbBtn->sizePolicy().hasHeightForWidth());
        f_customerDbBtn->setSizePolicy(sizePolicy1);
        f_customerDbBtn->setFrameShape(QFrame::StyledPanel);
        f_customerDbBtn->setFrameShadow(QFrame::Raised);
        horizontalLayout_19 = new QHBoxLayout(f_customerDbBtn);
        horizontalLayout_19->setSpacing(5);
        horizontalLayout_19->setObjectName(QString::fromUtf8("horizontalLayout_19"));
        horizontalLayout_19->setContentsMargins(0, 0, 0, 0);
        btn_customerAdd = new QPushButton(f_customerDbBtn);
        btn_customerAdd->setObjectName(QString::fromUtf8("btn_customerAdd"));
        btn_customerAdd->setIcon(icon34);
        btn_customerAdd->setIconSize(QSize(32, 32));

        horizontalLayout_19->addWidget(btn_customerAdd);

        btn_customerEdit = new QPushButton(f_customerDbBtn);
        btn_customerEdit->setObjectName(QString::fromUtf8("btn_customerEdit"));
        btn_customerEdit->setEnabled(false);
        btn_customerEdit->setIcon(icon35);
        btn_customerEdit->setIconSize(QSize(32, 32));

        horizontalLayout_19->addWidget(btn_customerEdit);

        btn_customerDelete = new QPushButton(f_customerDbBtn);
        btn_customerDelete->setObjectName(QString::fromUtf8("btn_customerDelete"));
        btn_customerDelete->setEnabled(false);
        btn_customerDelete->setIcon(icon20);
        btn_customerDelete->setIconSize(QSize(32, 32));

        horizontalLayout_19->addWidget(btn_customerDelete);

        btn_customerClear = new QPushButton(f_customerDbBtn);
        btn_customerClear->setObjectName(QString::fromUtf8("btn_customerClear"));
        btn_customerClear->setEnabled(true);
        btn_customerClear->setIcon(icon21);
        btn_customerClear->setIconSize(QSize(32, 32));

        horizontalLayout_19->addWidget(btn_customerClear);


        verticalLayout_40->addWidget(f_customerDbBtn);


        horizontalLayout_10->addWidget(f_customerInput);

        f_cutosmerDb = new QFrame(tab_customer);
        f_cutosmerDb->setObjectName(QString::fromUtf8("f_cutosmerDb"));
        f_cutosmerDb->setFrameShape(QFrame::StyledPanel);
        f_cutosmerDb->setFrameShadow(QFrame::Raised);
        verticalLayout_23 = new QVBoxLayout(f_cutosmerDb);
        verticalLayout_23->setObjectName(QString::fromUtf8("verticalLayout_23"));
        tw_customer = new QTableWidget(f_cutosmerDb);
        tw_customer->setObjectName(QString::fromUtf8("tw_customer"));
        tw_customer->setFont(font8);
        tw_customer->setEditTriggers(QAbstractItemView::NoEditTriggers);
        tw_customer->setSelectionMode(QAbstractItemView::SingleSelection);
        tw_customer->setSelectionBehavior(QAbstractItemView::SelectRows);
        tw_customer->horizontalHeader()->setProperty("showSortIndicator", QVariant(true));
        tw_customer->verticalHeader()->setCascadingSectionResizes(true);
        tw_customer->verticalHeader()->setProperty("showSortIndicator", QVariant(false));

        verticalLayout_23->addWidget(tw_customer);


        horizontalLayout_10->addWidget(f_cutosmerDb);

        QIcon icon46;
        icon46.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-comment-user.svg"), QSize(), QIcon::Normal, QIcon::Off);
        tw_database->addTab(tab_customer, icon46, QString());
        tab_worker = new QWidget();
        tab_worker->setObjectName(QString::fromUtf8("tab_worker"));
        horizontalLayout_11 = new QHBoxLayout(tab_worker);
        horizontalLayout_11->setObjectName(QString::fromUtf8("horizontalLayout_11"));
        f_workerInput = new QFrame(tab_worker);
        f_workerInput->setObjectName(QString::fromUtf8("f_workerInput"));
        f_workerInput->setStyleSheet(QString::fromUtf8("QFrame\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	\n"
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
"QComboBox\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}"));
        f_workerInput->setFrameShape(QFrame::StyledPanel);
        f_workerInput->setFrameShadow(QFrame::Raised);
        verticalLayout_35 = new QVBoxLayout(f_workerInput);
        verticalLayout_35->setObjectName(QString::fromUtf8("verticalLayout_35"));
        gb_worker = new QGroupBox(f_workerInput);
        gb_worker->setObjectName(QString::fromUtf8("gb_worker"));
        gb_worker->setFont(font5);
        gb_worker->setStyleSheet(QString::fromUtf8(""));
        verticalLayout_25 = new QVBoxLayout(gb_worker);
        verticalLayout_25->setObjectName(QString::fromUtf8("verticalLayout_25"));
        f_workerPic = new QFrame(gb_worker);
        f_workerPic->setObjectName(QString::fromUtf8("f_workerPic"));
        sizePolicy12.setHeightForWidth(f_workerPic->sizePolicy().hasHeightForWidth());
        f_workerPic->setSizePolicy(sizePolicy12);
        f_workerPic->setMinimumSize(QSize(50, 50));
        f_workerPic->setMaximumSize(QSize(800, 300));
        f_workerPic->setLayoutDirection(Qt::LeftToRight);
        f_workerPic->setStyleSheet(QString::fromUtf8(""));
        f_workerPic->setFrameShape(QFrame::StyledPanel);
        f_workerPic->setFrameShadow(QFrame::Raised);
        horizontalLayout_28 = new QHBoxLayout(f_workerPic);
        horizontalLayout_28->setSpacing(0);
        horizontalLayout_28->setObjectName(QString::fromUtf8("horizontalLayout_28"));
        horizontalLayout_28->setSizeConstraint(QLayout::SetMinimumSize);
        horizontalLayout_28->setContentsMargins(0, 0, 0, 0);
        l_workerPicture = new QLabel(f_workerPic);
        l_workerPicture->setObjectName(QString::fromUtf8("l_workerPicture"));
        sizePolicy.setHeightForWidth(l_workerPicture->sizePolicy().hasHeightForWidth());
        l_workerPicture->setSizePolicy(sizePolicy);
        l_workerPicture->setMinimumSize(QSize(50, 50));
        l_workerPicture->setMaximumSize(QSize(300, 300));
        l_workerPicture->setBaseSize(QSize(200, 200));
        l_workerPicture->setFont(font14);
        l_workerPicture->setLayoutDirection(Qt::LeftToRight);
        l_workerPicture->setAutoFillBackground(false);
        l_workerPicture->setStyleSheet(QString::fromUtf8(""));
        l_workerPicture->setFrameShape(QFrame::Box);
        l_workerPicture->setFrameShadow(QFrame::Plain);
        l_workerPicture->setScaledContents(true);
        l_workerPicture->setAlignment(Qt::AlignCenter);
        l_workerPicture->setWordWrap(false);

        horizontalLayout_28->addWidget(l_workerPicture);

        f_workerPictureSetting = new QFrame(f_workerPic);
        f_workerPictureSetting->setObjectName(QString::fromUtf8("f_workerPictureSetting"));
        f_workerPictureSetting->setFrameShape(QFrame::StyledPanel);
        f_workerPictureSetting->setFrameShadow(QFrame::Raised);
        verticalLayout_46 = new QVBoxLayout(f_workerPictureSetting);
        verticalLayout_46->setObjectName(QString::fromUtf8("verticalLayout_46"));
        btn_workerPicture = new QPushButton(f_workerPictureSetting);
        btn_workerPicture->setObjectName(QString::fromUtf8("btn_workerPicture"));
        sizePolicy12.setHeightForWidth(btn_workerPicture->sizePolicy().hasHeightForWidth());
        btn_workerPicture->setSizePolicy(sizePolicy12);
        btn_workerPicture->setIcon(icon39);
        btn_workerPicture->setIconSize(QSize(32, 32));

        verticalLayout_46->addWidget(btn_workerPicture);

        btn_workerPictureClear = new QPushButton(f_workerPictureSetting);
        btn_workerPictureClear->setObjectName(QString::fromUtf8("btn_workerPictureClear"));
        sizePolicy12.setHeightForWidth(btn_workerPictureClear->sizePolicy().hasHeightForWidth());
        btn_workerPictureClear->setSizePolicy(sizePolicy12);
        btn_workerPictureClear->setIcon(icon21);
        btn_workerPictureClear->setIconSize(QSize(32, 32));

        verticalLayout_46->addWidget(btn_workerPictureClear);


        horizontalLayout_28->addWidget(f_workerPictureSetting);


        verticalLayout_25->addWidget(f_workerPic);

        le_workerName = new QLineEdit(gb_worker);
        le_workerName->setObjectName(QString::fromUtf8("le_workerName"));
        le_workerName->setMaxLength(40);
        le_workerName->setClearButtonEnabled(true);

        verticalLayout_25->addWidget(le_workerName);

        cb_workerCategory = new QComboBox(gb_worker);
        cb_workerCategory->setObjectName(QString::fromUtf8("cb_workerCategory"));

        verticalLayout_25->addWidget(cb_workerCategory);

        le_workerUsername = new QLineEdit(gb_worker);
        le_workerUsername->setObjectName(QString::fromUtf8("le_workerUsername"));
        le_workerUsername->setMaxLength(20);
        le_workerUsername->setClearButtonEnabled(true);

        verticalLayout_25->addWidget(le_workerUsername);

        le_workerPassword = new QLineEdit(gb_worker);
        le_workerPassword->setObjectName(QString::fromUtf8("le_workerPassword"));
        le_workerPassword->setInputMethodHints(Qt::ImhHiddenText|Qt::ImhNoAutoUppercase|Qt::ImhNoPredictiveText|Qt::ImhSensitiveData);
        le_workerPassword->setMaxLength(20);
        le_workerPassword->setEchoMode(QLineEdit::Password);
        le_workerPassword->setClearButtonEnabled(true);

        verticalLayout_25->addWidget(le_workerPassword);

        le_workerPhone = new QLineEdit(gb_worker);
        le_workerPhone->setObjectName(QString::fromUtf8("le_workerPhone"));
        le_workerPhone->setMaxLength(20);
        le_workerPhone->setClearButtonEnabled(true);

        verticalLayout_25->addWidget(le_workerPhone);

        le_workerAddress = new QLineEdit(gb_worker);
        le_workerAddress->setObjectName(QString::fromUtf8("le_workerAddress"));
        le_workerAddress->setMaxLength(250);
        le_workerAddress->setClearButtonEnabled(true);

        verticalLayout_25->addWidget(le_workerAddress);

        le_workerSalary = new QLineEdit(gb_worker);
        le_workerSalary->setObjectName(QString::fromUtf8("le_workerSalary"));

        verticalLayout_25->addWidget(le_workerSalary);

        le_workerScore = new QLineEdit(gb_worker);
        le_workerScore->setObjectName(QString::fromUtf8("le_workerScore"));
        le_workerScore->setMaxLength(20);
        le_workerScore->setClearButtonEnabled(true);

        verticalLayout_25->addWidget(le_workerScore);

        frame_33 = new QFrame(gb_worker);
        frame_33->setObjectName(QString::fromUtf8("frame_33"));
        sizePolicy1.setHeightForWidth(frame_33->sizePolicy().hasHeightForWidth());
        frame_33->setSizePolicy(sizePolicy1);
        frame_33->setFrameShape(QFrame::StyledPanel);
        frame_33->setFrameShadow(QFrame::Raised);
        horizontalLayout_58 = new QHBoxLayout(frame_33);
        horizontalLayout_58->setObjectName(QString::fromUtf8("horizontalLayout_58"));
        le_workerCv = new QLineEdit(frame_33);
        le_workerCv->setObjectName(QString::fromUtf8("le_workerCv"));
        le_workerCv->setEnabled(false);
        le_workerCv->setMaxLength(20);
        le_workerCv->setClearButtonEnabled(true);

        horizontalLayout_58->addWidget(le_workerCv);

        btn_workerAddCv = new QPushButton(frame_33);
        btn_workerAddCv->setObjectName(QString::fromUtf8("btn_workerAddCv"));
        sizePolicy12.setHeightForWidth(btn_workerAddCv->sizePolicy().hasHeightForWidth());
        btn_workerAddCv->setSizePolicy(sizePolicy12);
        QIcon icon47;
        icon47.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-file-add.svg"), QSize(), QIcon::Normal, QIcon::Off);
        btn_workerAddCv->setIcon(icon47);
        btn_workerAddCv->setIconSize(QSize(32, 32));

        horizontalLayout_58->addWidget(btn_workerAddCv);

        btn_workerOpenCv = new QPushButton(frame_33);
        btn_workerOpenCv->setObjectName(QString::fromUtf8("btn_workerOpenCv"));
        sizePolicy12.setHeightForWidth(btn_workerOpenCv->sizePolicy().hasHeightForWidth());
        btn_workerOpenCv->setSizePolicy(sizePolicy12);
        QIcon icon48;
        icon48.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-search-alt.svg"), QSize(), QIcon::Normal, QIcon::Off);
        btn_workerOpenCv->setIcon(icon48);
        btn_workerOpenCv->setIconSize(QSize(32, 32));

        horizontalLayout_58->addWidget(btn_workerOpenCv);

        btn_workerClearCv = new QPushButton(frame_33);
        btn_workerClearCv->setObjectName(QString::fromUtf8("btn_workerClearCv"));
        sizePolicy12.setHeightForWidth(btn_workerClearCv->sizePolicy().hasHeightForWidth());
        btn_workerClearCv->setSizePolicy(sizePolicy12);
        btn_workerClearCv->setIcon(icon21);
        btn_workerClearCv->setIconSize(QSize(32, 32));

        horizontalLayout_58->addWidget(btn_workerClearCv);


        verticalLayout_25->addWidget(frame_33);


        verticalLayout_35->addWidget(gb_worker);

        f_workerDbBtn = new QFrame(f_workerInput);
        f_workerDbBtn->setObjectName(QString::fromUtf8("f_workerDbBtn"));
        sizePolicy1.setHeightForWidth(f_workerDbBtn->sizePolicy().hasHeightForWidth());
        f_workerDbBtn->setSizePolicy(sizePolicy1);
        f_workerDbBtn->setFrameShape(QFrame::StyledPanel);
        f_workerDbBtn->setFrameShadow(QFrame::Raised);
        horizontalLayout_20 = new QHBoxLayout(f_workerDbBtn);
        horizontalLayout_20->setSpacing(5);
        horizontalLayout_20->setObjectName(QString::fromUtf8("horizontalLayout_20"));
        horizontalLayout_20->setContentsMargins(0, 0, 0, 0);
        btn_workerAdd = new QPushButton(f_workerDbBtn);
        btn_workerAdd->setObjectName(QString::fromUtf8("btn_workerAdd"));
        btn_workerAdd->setIcon(icon34);
        btn_workerAdd->setIconSize(QSize(32, 32));

        horizontalLayout_20->addWidget(btn_workerAdd);

        btn_workerEdit = new QPushButton(f_workerDbBtn);
        btn_workerEdit->setObjectName(QString::fromUtf8("btn_workerEdit"));
        btn_workerEdit->setEnabled(false);
        btn_workerEdit->setIcon(icon35);
        btn_workerEdit->setIconSize(QSize(32, 32));

        horizontalLayout_20->addWidget(btn_workerEdit);

        btn_workerDelete = new QPushButton(f_workerDbBtn);
        btn_workerDelete->setObjectName(QString::fromUtf8("btn_workerDelete"));
        btn_workerDelete->setEnabled(false);
        btn_workerDelete->setIcon(icon20);
        btn_workerDelete->setIconSize(QSize(32, 32));

        horizontalLayout_20->addWidget(btn_workerDelete);

        btn_workerClear = new QPushButton(f_workerDbBtn);
        btn_workerClear->setObjectName(QString::fromUtf8("btn_workerClear"));
        btn_workerClear->setEnabled(true);
        btn_workerClear->setIcon(icon21);
        btn_workerClear->setIconSize(QSize(32, 32));

        horizontalLayout_20->addWidget(btn_workerClear);


        verticalLayout_35->addWidget(f_workerDbBtn);


        horizontalLayout_11->addWidget(f_workerInput);

        f_workerDb = new QFrame(tab_worker);
        f_workerDb->setObjectName(QString::fromUtf8("f_workerDb"));
        f_workerDb->setFrameShape(QFrame::StyledPanel);
        f_workerDb->setFrameShadow(QFrame::Raised);
        verticalLayout_30 = new QVBoxLayout(f_workerDb);
        verticalLayout_30->setObjectName(QString::fromUtf8("verticalLayout_30"));
        tw_worker = new QTableWidget(f_workerDb);
        tw_worker->setObjectName(QString::fromUtf8("tw_worker"));
        tw_worker->setFont(font8);
        tw_worker->setEditTriggers(QAbstractItemView::NoEditTriggers);
        tw_worker->setSelectionMode(QAbstractItemView::SingleSelection);
        tw_worker->setSelectionBehavior(QAbstractItemView::SelectRows);
        tw_worker->horizontalHeader()->setProperty("showSortIndicator", QVariant(true));
        tw_worker->verticalHeader()->setCascadingSectionResizes(true);
        tw_worker->verticalHeader()->setProperty("showSortIndicator", QVariant(false));

        verticalLayout_30->addWidget(tw_worker);


        horizontalLayout_11->addWidget(f_workerDb);

        QIcon icon49;
        icon49.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-id-badge.svg"), QSize(), QIcon::Normal, QIcon::Off);
        tw_database->addTab(tab_worker, icon49, QString());
        tab_category = new QWidget();
        tab_category->setObjectName(QString::fromUtf8("tab_category"));
        horizontalLayout_14 = new QHBoxLayout(tab_category);
        horizontalLayout_14->setObjectName(QString::fromUtf8("horizontalLayout_14"));
        f_categoryInput = new QFrame(tab_category);
        f_categoryInput->setObjectName(QString::fromUtf8("f_categoryInput"));
        f_categoryInput->setStyleSheet(QString::fromUtf8("QFrame\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	\n"
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
"}"));
        f_categoryInput->setFrameShape(QFrame::StyledPanel);
        f_categoryInput->setFrameShadow(QFrame::Raised);
        verticalLayout_37 = new QVBoxLayout(f_categoryInput);
        verticalLayout_37->setObjectName(QString::fromUtf8("verticalLayout_37"));
        gb_category = new QGroupBox(f_categoryInput);
        gb_category->setObjectName(QString::fromUtf8("gb_category"));
        gb_category->setFont(font5);
        gb_category->setStyleSheet(QString::fromUtf8("QLineEdit\n"
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
"}"));
        verticalLayout_28 = new QVBoxLayout(gb_category);
        verticalLayout_28->setObjectName(QString::fromUtf8("verticalLayout_28"));
        le_categoryName = new QLineEdit(gb_category);
        le_categoryName->setObjectName(QString::fromUtf8("le_categoryName"));
        le_categoryName->setMaxLength(20);
        le_categoryName->setClearButtonEnabled(true);

        verticalLayout_28->addWidget(le_categoryName);

        frame_32 = new QFrame(gb_category);
        frame_32->setObjectName(QString::fromUtf8("frame_32"));
        frame_32->setFrameShape(QFrame::StyledPanel);
        frame_32->setFrameShadow(QFrame::Raised);
        gridLayout_24 = new QGridLayout(frame_32);
        gridLayout_24->setObjectName(QString::fromUtf8("gridLayout_24"));
        cb_categoryLevelCashier = new QCheckBox(frame_32);
        cb_categoryLevelCashier->setObjectName(QString::fromUtf8("cb_categoryLevelCashier"));
        cb_categoryLevelCashier->setIcon(icon3);
        cb_categoryLevelCashier->setIconSize(QSize(32, 32));

        gridLayout_24->addWidget(cb_categoryLevelCashier, 0, 1, 1, 1);

        cb_categoryLevelWaste = new QCheckBox(frame_32);
        cb_categoryLevelWaste->setObjectName(QString::fromUtf8("cb_categoryLevelWaste"));
        cb_categoryLevelWaste->setIcon(icon5);
        cb_categoryLevelWaste->setIconSize(QSize(32, 32));

        gridLayout_24->addWidget(cb_categoryLevelWaste, 1, 1, 1, 1);

        cb_categoryLevelTables = new QCheckBox(frame_32);
        cb_categoryLevelTables->setObjectName(QString::fromUtf8("cb_categoryLevelTables"));
        cb_categoryLevelTables->setIcon(icon2);
        cb_categoryLevelTables->setIconSize(QSize(32, 32));

        gridLayout_24->addWidget(cb_categoryLevelTables, 0, 0, 1, 1);

        cb_categoryLevelStock = new QCheckBox(frame_32);
        cb_categoryLevelStock->setObjectName(QString::fromUtf8("cb_categoryLevelStock"));
        cb_categoryLevelStock->setIcon(icon48);
        cb_categoryLevelStock->setIconSize(QSize(32, 32));

        gridLayout_24->addWidget(cb_categoryLevelStock, 2, 0, 1, 1);

        cb_categoryLevelReservation = new QCheckBox(frame_32);
        cb_categoryLevelReservation->setObjectName(QString::fromUtf8("cb_categoryLevelReservation"));
        cb_categoryLevelReservation->setIcon(icon4);
        cb_categoryLevelReservation->setIconSize(QSize(32, 32));

        gridLayout_24->addWidget(cb_categoryLevelReservation, 1, 0, 1, 1);

        cb_categoryLevelReceipt = new QCheckBox(frame_32);
        cb_categoryLevelReceipt->setObjectName(QString::fromUtf8("cb_categoryLevelReceipt"));
        cb_categoryLevelReceipt->setIcon(icon7);
        cb_categoryLevelReceipt->setIconSize(QSize(32, 32));

        gridLayout_24->addWidget(cb_categoryLevelReceipt, 2, 1, 1, 1);

        cb_categoryLevelDb = new QCheckBox(frame_32);
        cb_categoryLevelDb->setObjectName(QString::fromUtf8("cb_categoryLevelDb"));
        cb_categoryLevelDb->setIcon(icon8);
        cb_categoryLevelDb->setIconSize(QSize(32, 32));

        gridLayout_24->addWidget(cb_categoryLevelDb, 3, 0, 1, 1);

        cb_categoryLevelPhone = new QCheckBox(frame_32);
        cb_categoryLevelPhone->setObjectName(QString::fromUtf8("cb_categoryLevelPhone"));
        cb_categoryLevelPhone->setIcon(icon9);
        cb_categoryLevelPhone->setIconSize(QSize(32, 32));

        gridLayout_24->addWidget(cb_categoryLevelPhone, 3, 1, 1, 1);

        cb_categoryLevelStat = new QCheckBox(frame_32);
        cb_categoryLevelStat->setObjectName(QString::fromUtf8("cb_categoryLevelStat"));
        cb_categoryLevelStat->setIcon(icon10);
        cb_categoryLevelStat->setIconSize(QSize(32, 32));

        gridLayout_24->addWidget(cb_categoryLevelStat, 4, 0, 1, 2);


        verticalLayout_28->addWidget(frame_32);


        verticalLayout_37->addWidget(gb_category);

        f_categoryDbBtn = new QFrame(f_categoryInput);
        f_categoryDbBtn->setObjectName(QString::fromUtf8("f_categoryDbBtn"));
        sizePolicy1.setHeightForWidth(f_categoryDbBtn->sizePolicy().hasHeightForWidth());
        f_categoryDbBtn->setSizePolicy(sizePolicy1);
        f_categoryDbBtn->setFrameShape(QFrame::StyledPanel);
        f_categoryDbBtn->setFrameShadow(QFrame::Raised);
        horizontalLayout_23 = new QHBoxLayout(f_categoryDbBtn);
        horizontalLayout_23->setSpacing(5);
        horizontalLayout_23->setObjectName(QString::fromUtf8("horizontalLayout_23"));
        horizontalLayout_23->setContentsMargins(0, 0, 0, 0);
        btn_categoryAdd = new QPushButton(f_categoryDbBtn);
        btn_categoryAdd->setObjectName(QString::fromUtf8("btn_categoryAdd"));
        btn_categoryAdd->setIcon(icon34);
        btn_categoryAdd->setIconSize(QSize(32, 32));

        horizontalLayout_23->addWidget(btn_categoryAdd);

        btn_categoryEdit = new QPushButton(f_categoryDbBtn);
        btn_categoryEdit->setObjectName(QString::fromUtf8("btn_categoryEdit"));
        btn_categoryEdit->setEnabled(false);
        btn_categoryEdit->setIcon(icon35);
        btn_categoryEdit->setIconSize(QSize(32, 32));

        horizontalLayout_23->addWidget(btn_categoryEdit);

        btn_categoryDelete = new QPushButton(f_categoryDbBtn);
        btn_categoryDelete->setObjectName(QString::fromUtf8("btn_categoryDelete"));
        btn_categoryDelete->setEnabled(false);
        btn_categoryDelete->setIcon(icon20);
        btn_categoryDelete->setIconSize(QSize(32, 32));

        horizontalLayout_23->addWidget(btn_categoryDelete);

        btn_categoryClear = new QPushButton(f_categoryDbBtn);
        btn_categoryClear->setObjectName(QString::fromUtf8("btn_categoryClear"));
        btn_categoryClear->setEnabled(true);
        btn_categoryClear->setIcon(icon21);
        btn_categoryClear->setIconSize(QSize(32, 32));

        horizontalLayout_23->addWidget(btn_categoryClear);


        verticalLayout_37->addWidget(f_categoryDbBtn);


        horizontalLayout_14->addWidget(f_categoryInput);

        f_categoryDb = new QFrame(tab_category);
        f_categoryDb->setObjectName(QString::fromUtf8("f_categoryDb"));
        f_categoryDb->setFrameShape(QFrame::StyledPanel);
        f_categoryDb->setFrameShadow(QFrame::Raised);
        verticalLayout_33 = new QVBoxLayout(f_categoryDb);
        verticalLayout_33->setObjectName(QString::fromUtf8("verticalLayout_33"));
        tw_category = new QTableWidget(f_categoryDb);
        tw_category->setObjectName(QString::fromUtf8("tw_category"));
        tw_category->setFont(font8);
        tw_category->setEditTriggers(QAbstractItemView::NoEditTriggers);
        tw_category->setSelectionMode(QAbstractItemView::SingleSelection);
        tw_category->setSelectionBehavior(QAbstractItemView::SelectRows);
        tw_category->horizontalHeader()->setProperty("showSortIndicator", QVariant(true));
        tw_category->verticalHeader()->setCascadingSectionResizes(true);
        tw_category->verticalHeader()->setProperty("showSortIndicator", QVariant(false));

        verticalLayout_33->addWidget(tw_category);


        horizontalLayout_14->addWidget(f_categoryDb);

        QIcon icon50;
        icon50.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-diploma.svg"), QSize(), QIcon::Normal, QIcon::Off);
        tw_database->addTab(tab_category, icon50, QString());
        tab_sell = new QWidget();
        tab_sell->setObjectName(QString::fromUtf8("tab_sell"));
        horizontalLayout_12 = new QHBoxLayout(tab_sell);
        horizontalLayout_12->setObjectName(QString::fromUtf8("horizontalLayout_12"));
        f_sellInput = new QFrame(tab_sell);
        f_sellInput->setObjectName(QString::fromUtf8("f_sellInput"));
        f_sellInput->setStyleSheet(QString::fromUtf8("QFrame\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	\n"
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
"}"));
        f_sellInput->setFrameShape(QFrame::StyledPanel);
        f_sellInput->setFrameShadow(QFrame::Raised);
        verticalLayout_39 = new QVBoxLayout(f_sellInput);
        verticalLayout_39->setObjectName(QString::fromUtf8("verticalLayout_39"));
        gb_sell = new QGroupBox(f_sellInput);
        gb_sell->setObjectName(QString::fromUtf8("gb_sell"));
        gb_sell->setFont(font5);
        gb_sell->setStyleSheet(QString::fromUtf8("QLineEdit\n"
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
"}"));
        verticalLayout_26 = new QVBoxLayout(gb_sell);
        verticalLayout_26->setObjectName(QString::fromUtf8("verticalLayout_26"));
        cb_sellIdWorker = new QComboBox(gb_sell);
        cb_sellIdWorker->setObjectName(QString::fromUtf8("cb_sellIdWorker"));

        verticalLayout_26->addWidget(cb_sellIdWorker);

        cb_sellIdCustomer = new QComboBox(gb_sell);
        cb_sellIdCustomer->setObjectName(QString::fromUtf8("cb_sellIdCustomer"));

        verticalLayout_26->addWidget(cb_sellIdCustomer);

        dte_sellDate = new QDateTimeEdit(gb_sell);
        dte_sellDate->setObjectName(QString::fromUtf8("dte_sellDate"));
        dte_sellDate->setFont(font5);
        dte_sellDate->setCalendarPopup(true);

        verticalLayout_26->addWidget(dte_sellDate);

        le_sellTotal = new QLineEdit(gb_sell);
        le_sellTotal->setObjectName(QString::fromUtf8("le_sellTotal"));
        le_sellTotal->setMaxLength(20);
        le_sellTotal->setClearButtonEnabled(true);

        verticalLayout_26->addWidget(le_sellTotal);

        le_sellNbCovers = new QLineEdit(gb_sell);
        le_sellNbCovers->setObjectName(QString::fromUtf8("le_sellNbCovers"));
        le_sellNbCovers->setMaxLength(20);
        le_sellNbCovers->setClearButtonEnabled(true);

        verticalLayout_26->addWidget(le_sellNbCovers);


        verticalLayout_39->addWidget(gb_sell);

        f_sellDbBtn = new QFrame(f_sellInput);
        f_sellDbBtn->setObjectName(QString::fromUtf8("f_sellDbBtn"));
        sizePolicy1.setHeightForWidth(f_sellDbBtn->sizePolicy().hasHeightForWidth());
        f_sellDbBtn->setSizePolicy(sizePolicy1);
        f_sellDbBtn->setFrameShape(QFrame::StyledPanel);
        f_sellDbBtn->setFrameShadow(QFrame::Raised);
        horizontalLayout_21 = new QHBoxLayout(f_sellDbBtn);
        horizontalLayout_21->setSpacing(5);
        horizontalLayout_21->setObjectName(QString::fromUtf8("horizontalLayout_21"));
        horizontalLayout_21->setContentsMargins(0, 0, 0, 0);
        btn_sellAdd = new QPushButton(f_sellDbBtn);
        btn_sellAdd->setObjectName(QString::fromUtf8("btn_sellAdd"));
        btn_sellAdd->setIcon(icon34);
        btn_sellAdd->setIconSize(QSize(32, 32));

        horizontalLayout_21->addWidget(btn_sellAdd);

        btn_sellEdit = new QPushButton(f_sellDbBtn);
        btn_sellEdit->setObjectName(QString::fromUtf8("btn_sellEdit"));
        btn_sellEdit->setEnabled(false);
        btn_sellEdit->setIcon(icon35);
        btn_sellEdit->setIconSize(QSize(32, 32));

        horizontalLayout_21->addWidget(btn_sellEdit);

        btn_sellDelete = new QPushButton(f_sellDbBtn);
        btn_sellDelete->setObjectName(QString::fromUtf8("btn_sellDelete"));
        btn_sellDelete->setEnabled(false);
        btn_sellDelete->setIcon(icon20);
        btn_sellDelete->setIconSize(QSize(32, 32));

        horizontalLayout_21->addWidget(btn_sellDelete);

        btn_sellClear = new QPushButton(f_sellDbBtn);
        btn_sellClear->setObjectName(QString::fromUtf8("btn_sellClear"));
        btn_sellClear->setEnabled(true);
        btn_sellClear->setIcon(icon21);
        btn_sellClear->setIconSize(QSize(32, 32));

        horizontalLayout_21->addWidget(btn_sellClear);

        btn_sellShow = new QPushButton(f_sellDbBtn);
        btn_sellShow->setObjectName(QString::fromUtf8("btn_sellShow"));
        btn_sellShow->setEnabled(false);
        QIcon icon51;
        icon51.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-upload.svg"), QSize(), QIcon::Normal, QIcon::Off);
        btn_sellShow->setIcon(icon51);
        btn_sellShow->setIconSize(QSize(32, 32));

        horizontalLayout_21->addWidget(btn_sellShow);

        btn_sellLoad = new QPushButton(f_sellDbBtn);
        btn_sellLoad->setObjectName(QString::fromUtf8("btn_sellLoad"));
        btn_sellLoad->setEnabled(false);
        QIcon icon52;
        icon52.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-calculator.svg"), QSize(), QIcon::Normal, QIcon::Off);
        btn_sellLoad->setIcon(icon52);
        btn_sellLoad->setIconSize(QSize(32, 32));

        horizontalLayout_21->addWidget(btn_sellLoad);


        verticalLayout_39->addWidget(f_sellDbBtn);


        horizontalLayout_12->addWidget(f_sellInput);

        f_sellDb = new QFrame(tab_sell);
        f_sellDb->setObjectName(QString::fromUtf8("f_sellDb"));
        f_sellDb->setStyleSheet(QString::fromUtf8(""));
        f_sellDb->setFrameShape(QFrame::StyledPanel);
        f_sellDb->setFrameShadow(QFrame::Raised);
        verticalLayout_31 = new QVBoxLayout(f_sellDb);
        verticalLayout_31->setObjectName(QString::fromUtf8("verticalLayout_31"));
        tw_sell = new QTableWidget(f_sellDb);
        tw_sell->setObjectName(QString::fromUtf8("tw_sell"));
        tw_sell->setFont(font8);
        tw_sell->setEditTriggers(QAbstractItemView::NoEditTriggers);
        tw_sell->setSelectionMode(QAbstractItemView::SingleSelection);
        tw_sell->setSelectionBehavior(QAbstractItemView::SelectRows);
        tw_sell->horizontalHeader()->setProperty("showSortIndicator", QVariant(true));
        tw_sell->verticalHeader()->setCascadingSectionResizes(true);
        tw_sell->verticalHeader()->setProperty("showSortIndicator", QVariant(false));

        verticalLayout_31->addWidget(tw_sell);


        horizontalLayout_12->addWidget(f_sellDb);

        tw_database->addTab(tab_sell, icon27, QString());
        tab_table = new QWidget();
        tab_table->setObjectName(QString::fromUtf8("tab_table"));
        horizontalLayout_13 = new QHBoxLayout(tab_table);
        horizontalLayout_13->setObjectName(QString::fromUtf8("horizontalLayout_13"));
        f_tableInput = new QFrame(tab_table);
        f_tableInput->setObjectName(QString::fromUtf8("f_tableInput"));
        f_tableInput->setStyleSheet(QString::fromUtf8("QFrame\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	\n"
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
"}"));
        f_tableInput->setFrameShape(QFrame::StyledPanel);
        f_tableInput->setFrameShadow(QFrame::Raised);
        verticalLayout_38 = new QVBoxLayout(f_tableInput);
        verticalLayout_38->setObjectName(QString::fromUtf8("verticalLayout_38"));
        gb_expense_6 = new QGroupBox(f_tableInput);
        gb_expense_6->setObjectName(QString::fromUtf8("gb_expense_6"));
        gb_expense_6->setFont(font5);
        gb_expense_6->setStyleSheet(QString::fromUtf8("QLineEdit\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
""));
        verticalLayout_27 = new QVBoxLayout(gb_expense_6);
        verticalLayout_27->setObjectName(QString::fromUtf8("verticalLayout_27"));
        le_tableName = new QLineEdit(gb_expense_6);
        le_tableName->setObjectName(QString::fromUtf8("le_tableName"));
        le_tableName->setMaxLength(20);
        le_tableName->setClearButtonEnabled(true);

        verticalLayout_27->addWidget(le_tableName);

        le_tableId = new QLineEdit(gb_expense_6);
        le_tableId->setObjectName(QString::fromUtf8("le_tableId"));
        le_tableId->setMaxLength(20);
        le_tableId->setClearButtonEnabled(true);

        verticalLayout_27->addWidget(le_tableId);

        le_tableSeats = new QLineEdit(gb_expense_6);
        le_tableSeats->setObjectName(QString::fromUtf8("le_tableSeats"));
        le_tableSeats->setMaxLength(20);
        le_tableSeats->setClearButtonEnabled(true);

        verticalLayout_27->addWidget(le_tableSeats);

        le_tableComment = new QLineEdit(gb_expense_6);
        le_tableComment->setObjectName(QString::fromUtf8("le_tableComment"));
        le_tableComment->setMaxLength(30);
        le_tableComment->setClearButtonEnabled(true);

        verticalLayout_27->addWidget(le_tableComment);


        verticalLayout_38->addWidget(gb_expense_6);

        f_tableDbBtn = new QFrame(f_tableInput);
        f_tableDbBtn->setObjectName(QString::fromUtf8("f_tableDbBtn"));
        sizePolicy1.setHeightForWidth(f_tableDbBtn->sizePolicy().hasHeightForWidth());
        f_tableDbBtn->setSizePolicy(sizePolicy1);
        f_tableDbBtn->setFrameShape(QFrame::StyledPanel);
        f_tableDbBtn->setFrameShadow(QFrame::Raised);
        horizontalLayout_22 = new QHBoxLayout(f_tableDbBtn);
        horizontalLayout_22->setSpacing(5);
        horizontalLayout_22->setObjectName(QString::fromUtf8("horizontalLayout_22"));
        horizontalLayout_22->setContentsMargins(0, 0, 0, 0);
        btn_tableAdd = new QPushButton(f_tableDbBtn);
        btn_tableAdd->setObjectName(QString::fromUtf8("btn_tableAdd"));
        btn_tableAdd->setIcon(icon34);
        btn_tableAdd->setIconSize(QSize(32, 32));

        horizontalLayout_22->addWidget(btn_tableAdd);

        btn_tableEdit = new QPushButton(f_tableDbBtn);
        btn_tableEdit->setObjectName(QString::fromUtf8("btn_tableEdit"));
        btn_tableEdit->setEnabled(false);
        btn_tableEdit->setIcon(icon35);
        btn_tableEdit->setIconSize(QSize(32, 32));

        horizontalLayout_22->addWidget(btn_tableEdit);

        btn_tableDelete = new QPushButton(f_tableDbBtn);
        btn_tableDelete->setObjectName(QString::fromUtf8("btn_tableDelete"));
        btn_tableDelete->setEnabled(false);
        btn_tableDelete->setIcon(icon20);
        btn_tableDelete->setIconSize(QSize(32, 32));

        horizontalLayout_22->addWidget(btn_tableDelete);

        btn_tableClear = new QPushButton(f_tableDbBtn);
        btn_tableClear->setObjectName(QString::fromUtf8("btn_tableClear"));
        btn_tableClear->setEnabled(true);
        btn_tableClear->setIcon(icon21);
        btn_tableClear->setIconSize(QSize(32, 32));

        horizontalLayout_22->addWidget(btn_tableClear);


        verticalLayout_38->addWidget(f_tableDbBtn);


        horizontalLayout_13->addWidget(f_tableInput);

        f_tableDb = new QFrame(tab_table);
        f_tableDb->setObjectName(QString::fromUtf8("f_tableDb"));
        f_tableDb->setFrameShape(QFrame::StyledPanel);
        f_tableDb->setFrameShadow(QFrame::Raised);
        verticalLayout_32 = new QVBoxLayout(f_tableDb);
        verticalLayout_32->setObjectName(QString::fromUtf8("verticalLayout_32"));
        tw_table = new QTableWidget(f_tableDb);
        tw_table->setObjectName(QString::fromUtf8("tw_table"));
        tw_table->setFont(font8);
        tw_table->setEditTriggers(QAbstractItemView::NoEditTriggers);
        tw_table->setSelectionMode(QAbstractItemView::SingleSelection);
        tw_table->setSelectionBehavior(QAbstractItemView::SelectRows);
        tw_table->horizontalHeader()->setProperty("showSortIndicator", QVariant(true));
        tw_table->verticalHeader()->setCascadingSectionResizes(true);
        tw_table->verticalHeader()->setProperty("showSortIndicator", QVariant(false));

        verticalLayout_32->addWidget(tw_table);


        horizontalLayout_13->addWidget(f_tableDb);

        tw_database->addTab(tab_table, icon2, QString());
        tab_pointer = new QWidget();
        tab_pointer->setObjectName(QString::fromUtf8("tab_pointer"));
        horizontalLayout_15 = new QHBoxLayout(tab_pointer);
        horizontalLayout_15->setObjectName(QString::fromUtf8("horizontalLayout_15"));
        f_pointerDb = new QFrame(tab_pointer);
        f_pointerDb->setObjectName(QString::fromUtf8("f_pointerDb"));
        f_pointerDb->setFrameShape(QFrame::StyledPanel);
        f_pointerDb->setFrameShadow(QFrame::Raised);
        verticalLayout_34 = new QVBoxLayout(f_pointerDb);
        verticalLayout_34->setObjectName(QString::fromUtf8("verticalLayout_34"));
        groupBox = new QGroupBox(f_pointerDb);
        groupBox->setObjectName(QString::fromUtf8("groupBox"));
        groupBox->setFont(font5);
        groupBox->setStyleSheet(QString::fromUtf8("QFrame\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	\n"
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
"QComboBox\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
""));
        verticalLayout_47 = new QVBoxLayout(groupBox);
        verticalLayout_47->setObjectName(QString::fromUtf8("verticalLayout_47"));
        tw_pointer = new QTableWidget(groupBox);
        tw_pointer->setObjectName(QString::fromUtf8("tw_pointer"));
        tw_pointer->setFont(font8);
        tw_pointer->setEditTriggers(QAbstractItemView::NoEditTriggers);
        tw_pointer->setSelectionMode(QAbstractItemView::SingleSelection);
        tw_pointer->setSelectionBehavior(QAbstractItemView::SelectRows);
        tw_pointer->horizontalHeader()->setProperty("showSortIndicator", QVariant(true));
        tw_pointer->verticalHeader()->setCascadingSectionResizes(true);
        tw_pointer->verticalHeader()->setProperty("showSortIndicator", QVariant(false));

        verticalLayout_47->addWidget(tw_pointer);


        verticalLayout_34->addWidget(groupBox);


        horizontalLayout_15->addWidget(f_pointerDb);

        tw_database->addTab(tab_pointer, icon48, QString());
        tab_stock = new QWidget();
        tab_stock->setObjectName(QString::fromUtf8("tab_stock"));
        horizontalLayout_60 = new QHBoxLayout(tab_stock);
        horizontalLayout_60->setObjectName(QString::fromUtf8("horizontalLayout_60"));
        f_tableInput_2 = new QFrame(tab_stock);
        f_tableInput_2->setObjectName(QString::fromUtf8("f_tableInput_2"));
        f_tableInput_2->setStyleSheet(QString::fromUtf8("QFrame\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	\n"
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
"\n"
"QComboBox\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}"));
        f_tableInput_2->setFrameShape(QFrame::StyledPanel);
        f_tableInput_2->setFrameShadow(QFrame::Raised);
        verticalLayout_42 = new QVBoxLayout(f_tableInput_2);
        verticalLayout_42->setObjectName(QString::fromUtf8("verticalLayout_42"));
        gb_stock = new QGroupBox(f_tableInput_2);
        gb_stock->setObjectName(QString::fromUtf8("gb_stock"));
        gb_stock->setFont(font5);
        gb_stock->setStyleSheet(QString::fromUtf8("QLineEdit\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
""));
        verticalLayout_79 = new QVBoxLayout(gb_stock);
        verticalLayout_79->setObjectName(QString::fromUtf8("verticalLayout_79"));
        le_stockProductName = new QLineEdit(gb_stock);
        le_stockProductName->setObjectName(QString::fromUtf8("le_stockProductName"));
        le_stockProductName->setMaxLength(20);
        le_stockProductName->setClearButtonEnabled(true);

        verticalLayout_79->addWidget(le_stockProductName);

        cb_stockCategory = new QComboBox(gb_stock);
        cb_stockCategory->setObjectName(QString::fromUtf8("cb_stockCategory"));

        verticalLayout_79->addWidget(cb_stockCategory);

        le_stockUnit = new QLineEdit(gb_stock);
        le_stockUnit->setObjectName(QString::fromUtf8("le_stockUnit"));
        le_stockUnit->setMaxLength(20);
        le_stockUnit->setClearButtonEnabled(true);

        verticalLayout_79->addWidget(le_stockUnit);

        le_stockQuantity = new QLineEdit(gb_stock);
        le_stockQuantity->setObjectName(QString::fromUtf8("le_stockQuantity"));
        le_stockQuantity->setMaxLength(30);
        le_stockQuantity->setClearButtonEnabled(true);

        verticalLayout_79->addWidget(le_stockQuantity);

        cb_stockIsIngredient = new QCheckBox(gb_stock);
        cb_stockIsIngredient->setObjectName(QString::fromUtf8("cb_stockIsIngredient"));
        cb_stockIsIngredient->setFont(font3);
        cb_stockIsIngredient->setLayoutDirection(Qt::LeftToRight);
        cb_stockIsIngredient->setIcon(icon44);
        cb_stockIsIngredient->setIconSize(QSize(32, 32));
        cb_stockIsIngredient->setChecked(true);

        verticalLayout_79->addWidget(cb_stockIsIngredient);


        verticalLayout_42->addWidget(gb_stock);

        f_tableDbBtn_2 = new QFrame(f_tableInput_2);
        f_tableDbBtn_2->setObjectName(QString::fromUtf8("f_tableDbBtn_2"));
        sizePolicy1.setHeightForWidth(f_tableDbBtn_2->sizePolicy().hasHeightForWidth());
        f_tableDbBtn_2->setSizePolicy(sizePolicy1);
        f_tableDbBtn_2->setFrameShape(QFrame::StyledPanel);
        f_tableDbBtn_2->setFrameShadow(QFrame::Raised);
        horizontalLayout_59 = new QHBoxLayout(f_tableDbBtn_2);
        horizontalLayout_59->setSpacing(5);
        horizontalLayout_59->setObjectName(QString::fromUtf8("horizontalLayout_59"));
        horizontalLayout_59->setContentsMargins(0, 0, 0, 0);
        btn_stockAdd = new QPushButton(f_tableDbBtn_2);
        btn_stockAdd->setObjectName(QString::fromUtf8("btn_stockAdd"));
        btn_stockAdd->setIcon(icon34);
        btn_stockAdd->setIconSize(QSize(32, 32));

        horizontalLayout_59->addWidget(btn_stockAdd);

        btn_stockEdit = new QPushButton(f_tableDbBtn_2);
        btn_stockEdit->setObjectName(QString::fromUtf8("btn_stockEdit"));
        btn_stockEdit->setEnabled(false);
        btn_stockEdit->setIcon(icon35);
        btn_stockEdit->setIconSize(QSize(32, 32));

        horizontalLayout_59->addWidget(btn_stockEdit);

        btn_stockDelete = new QPushButton(f_tableDbBtn_2);
        btn_stockDelete->setObjectName(QString::fromUtf8("btn_stockDelete"));
        btn_stockDelete->setEnabled(false);
        btn_stockDelete->setIcon(icon20);
        btn_stockDelete->setIconSize(QSize(32, 32));

        horizontalLayout_59->addWidget(btn_stockDelete);

        btn_stockClear = new QPushButton(f_tableDbBtn_2);
        btn_stockClear->setObjectName(QString::fromUtf8("btn_stockClear"));
        btn_stockClear->setEnabled(true);
        btn_stockClear->setIcon(icon21);
        btn_stockClear->setIconSize(QSize(32, 32));

        horizontalLayout_59->addWidget(btn_stockClear);


        verticalLayout_42->addWidget(f_tableDbBtn_2);


        horizontalLayout_60->addWidget(f_tableInput_2);

        f_stockDb = new QFrame(tab_stock);
        f_stockDb->setObjectName(QString::fromUtf8("f_stockDb"));
        f_stockDb->setFrameShape(QFrame::StyledPanel);
        f_stockDb->setFrameShadow(QFrame::Raised);
        verticalLayout_80 = new QVBoxLayout(f_stockDb);
        verticalLayout_80->setObjectName(QString::fromUtf8("verticalLayout_80"));
        tw_stockDb = new QTableWidget(f_stockDb);
        tw_stockDb->setObjectName(QString::fromUtf8("tw_stockDb"));
        tw_stockDb->setFont(font8);
        tw_stockDb->setEditTriggers(QAbstractItemView::NoEditTriggers);
        tw_stockDb->setSelectionMode(QAbstractItemView::SingleSelection);
        tw_stockDb->setSelectionBehavior(QAbstractItemView::SelectRows);
        tw_stockDb->horizontalHeader()->setProperty("showSortIndicator", QVariant(true));
        tw_stockDb->verticalHeader()->setCascadingSectionResizes(true);
        tw_stockDb->verticalHeader()->setProperty("showSortIndicator", QVariant(false));

        verticalLayout_80->addWidget(tw_stockDb);


        horizontalLayout_60->addWidget(f_stockDb);

        tw_database->addTab(tab_stock, icon6, QString());
        tab_uploader = new QWidget();
        tab_uploader->setObjectName(QString::fromUtf8("tab_uploader"));
        horizontalLayout_62 = new QHBoxLayout(tab_uploader);
        horizontalLayout_62->setObjectName(QString::fromUtf8("horizontalLayout_62"));
        f_tableInput_3 = new QFrame(tab_uploader);
        f_tableInput_3->setObjectName(QString::fromUtf8("f_tableInput_3"));
        f_tableInput_3->setStyleSheet(QString::fromUtf8("QFrame\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	\n"
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
"}"));
        f_tableInput_3->setFrameShape(QFrame::StyledPanel);
        f_tableInput_3->setFrameShadow(QFrame::Raised);
        verticalLayout_82 = new QVBoxLayout(f_tableInput_3);
        verticalLayout_82->setObjectName(QString::fromUtf8("verticalLayout_82"));
        gb_doccuments = new QGroupBox(f_tableInput_3);
        gb_doccuments->setObjectName(QString::fromUtf8("gb_doccuments"));
        gb_doccuments->setFont(font5);
        gb_doccuments->setStyleSheet(QString::fromUtf8("QLineEdit\n"
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
"}"));
        verticalLayout_83 = new QVBoxLayout(gb_doccuments);
        verticalLayout_83->setObjectName(QString::fromUtf8("verticalLayout_83"));
        le_docName = new QLineEdit(gb_doccuments);
        le_docName->setObjectName(QString::fromUtf8("le_docName"));
        le_docName->setMaxLength(80);
        le_docName->setClearButtonEnabled(true);

        verticalLayout_83->addWidget(le_docName);

        dte_docDate = new QDateTimeEdit(gb_doccuments);
        dte_docDate->setObjectName(QString::fromUtf8("dte_docDate"));
        dte_docDate->setFont(font5);
        dte_docDate->setCalendarPopup(true);

        verticalLayout_83->addWidget(dte_docDate);

        le_docComment = new QLineEdit(gb_doccuments);
        le_docComment->setObjectName(QString::fromUtf8("le_docComment"));
        le_docComment->setMaxLength(250);
        le_docComment->setClearButtonEnabled(true);

        verticalLayout_83->addWidget(le_docComment);

        frame_40 = new QFrame(gb_doccuments);
        frame_40->setObjectName(QString::fromUtf8("frame_40"));
        sizePolicy1.setHeightForWidth(frame_40->sizePolicy().hasHeightForWidth());
        frame_40->setSizePolicy(sizePolicy1);
        frame_40->setFrameShape(QFrame::StyledPanel);
        frame_40->setFrameShadow(QFrame::Raised);
        horizontalLayout_64 = new QHBoxLayout(frame_40);
        horizontalLayout_64->setObjectName(QString::fromUtf8("horizontalLayout_64"));
        le_docPath = new QLineEdit(frame_40);
        le_docPath->setObjectName(QString::fromUtf8("le_docPath"));
        le_docPath->setEnabled(false);
        le_docPath->setMaxLength(20);
        le_docPath->setClearButtonEnabled(true);

        horizontalLayout_64->addWidget(le_docPath);

        btn_docAddFile = new QPushButton(frame_40);
        btn_docAddFile->setObjectName(QString::fromUtf8("btn_docAddFile"));
        sizePolicy12.setHeightForWidth(btn_docAddFile->sizePolicy().hasHeightForWidth());
        btn_docAddFile->setSizePolicy(sizePolicy12);
        btn_docAddFile->setIcon(icon47);
        btn_docAddFile->setIconSize(QSize(32, 32));

        horizontalLayout_64->addWidget(btn_docAddFile);

        btn_docOpenFile = new QPushButton(frame_40);
        btn_docOpenFile->setObjectName(QString::fromUtf8("btn_docOpenFile"));
        sizePolicy12.setHeightForWidth(btn_docOpenFile->sizePolicy().hasHeightForWidth());
        btn_docOpenFile->setSizePolicy(sizePolicy12);
        btn_docOpenFile->setIcon(icon48);
        btn_docOpenFile->setIconSize(QSize(32, 32));

        horizontalLayout_64->addWidget(btn_docOpenFile);

        btn_docClearFile = new QPushButton(frame_40);
        btn_docClearFile->setObjectName(QString::fromUtf8("btn_docClearFile"));
        sizePolicy12.setHeightForWidth(btn_docClearFile->sizePolicy().hasHeightForWidth());
        btn_docClearFile->setSizePolicy(sizePolicy12);
        btn_docClearFile->setIcon(icon21);
        btn_docClearFile->setIconSize(QSize(32, 32));

        horizontalLayout_64->addWidget(btn_docClearFile);


        verticalLayout_83->addWidget(frame_40);


        verticalLayout_82->addWidget(gb_doccuments);

        f_tableDbBtn_3 = new QFrame(f_tableInput_3);
        f_tableDbBtn_3->setObjectName(QString::fromUtf8("f_tableDbBtn_3"));
        sizePolicy1.setHeightForWidth(f_tableDbBtn_3->sizePolicy().hasHeightForWidth());
        f_tableDbBtn_3->setSizePolicy(sizePolicy1);
        f_tableDbBtn_3->setFrameShape(QFrame::StyledPanel);
        f_tableDbBtn_3->setFrameShadow(QFrame::Raised);
        horizontalLayout_61 = new QHBoxLayout(f_tableDbBtn_3);
        horizontalLayout_61->setSpacing(5);
        horizontalLayout_61->setObjectName(QString::fromUtf8("horizontalLayout_61"));
        horizontalLayout_61->setContentsMargins(0, 0, 0, 0);
        btn_docAdd = new QPushButton(f_tableDbBtn_3);
        btn_docAdd->setObjectName(QString::fromUtf8("btn_docAdd"));
        btn_docAdd->setIcon(icon34);
        btn_docAdd->setIconSize(QSize(32, 32));

        horizontalLayout_61->addWidget(btn_docAdd);

        btn_docEdit = new QPushButton(f_tableDbBtn_3);
        btn_docEdit->setObjectName(QString::fromUtf8("btn_docEdit"));
        btn_docEdit->setEnabled(false);
        btn_docEdit->setIcon(icon35);
        btn_docEdit->setIconSize(QSize(32, 32));

        horizontalLayout_61->addWidget(btn_docEdit);

        btn_docDelete = new QPushButton(f_tableDbBtn_3);
        btn_docDelete->setObjectName(QString::fromUtf8("btn_docDelete"));
        btn_docDelete->setEnabled(false);
        btn_docDelete->setIcon(icon20);
        btn_docDelete->setIconSize(QSize(32, 32));

        horizontalLayout_61->addWidget(btn_docDelete);

        btn_docClear = new QPushButton(f_tableDbBtn_3);
        btn_docClear->setObjectName(QString::fromUtf8("btn_docClear"));
        btn_docClear->setEnabled(true);
        btn_docClear->setIcon(icon21);
        btn_docClear->setIconSize(QSize(32, 32));

        horizontalLayout_61->addWidget(btn_docClear);


        verticalLayout_82->addWidget(f_tableDbBtn_3);


        horizontalLayout_62->addWidget(f_tableInput_3);

        f_stockDb_2 = new QFrame(tab_uploader);
        f_stockDb_2->setObjectName(QString::fromUtf8("f_stockDb_2"));
        f_stockDb_2->setFrameShape(QFrame::StyledPanel);
        f_stockDb_2->setFrameShadow(QFrame::Raised);
        verticalLayout_81 = new QVBoxLayout(f_stockDb_2);
        verticalLayout_81->setObjectName(QString::fromUtf8("verticalLayout_81"));
        tw_documentDb = new QTableWidget(f_stockDb_2);
        tw_documentDb->setObjectName(QString::fromUtf8("tw_documentDb"));
        tw_documentDb->setFont(font8);
        tw_documentDb->setEditTriggers(QAbstractItemView::NoEditTriggers);
        tw_documentDb->setSelectionMode(QAbstractItemView::SingleSelection);
        tw_documentDb->setSelectionBehavior(QAbstractItemView::SelectRows);
        tw_documentDb->horizontalHeader()->setProperty("showSortIndicator", QVariant(true));
        tw_documentDb->verticalHeader()->setCascadingSectionResizes(true);
        tw_documentDb->verticalHeader()->setProperty("showSortIndicator", QVariant(false));

        verticalLayout_81->addWidget(tw_documentDb);


        horizontalLayout_62->addWidget(f_stockDb_2);

        tw_database->addTab(tab_uploader, icon51, QString());
        tab_tableOwnership = new QWidget();
        tab_tableOwnership->setObjectName(QString::fromUtf8("tab_tableOwnership"));
        horizontalLayout_67 = new QHBoxLayout(tab_tableOwnership);
        horizontalLayout_67->setObjectName(QString::fromUtf8("horizontalLayout_67"));
        f_tableOwnershipInput = new QFrame(tab_tableOwnership);
        f_tableOwnershipInput->setObjectName(QString::fromUtf8("f_tableOwnershipInput"));
        f_tableOwnershipInput->setStyleSheet(QString::fromUtf8("QFrame\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QGroupBox\n"
"{\n"
"	background-color: rgb(192, 192, 192)\n"
"}\n"
"\n"
"QPushButton\n"
"{ \n"
"	\n"
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
"}"));
        f_tableOwnershipInput->setFrameShape(QFrame::StyledPanel);
        f_tableOwnershipInput->setFrameShadow(QFrame::Raised);
        verticalLayout_88 = new QVBoxLayout(f_tableOwnershipInput);
        verticalLayout_88->setObjectName(QString::fromUtf8("verticalLayout_88"));
        gb_tableOwnership = new QGroupBox(f_tableOwnershipInput);
        gb_tableOwnership->setObjectName(QString::fromUtf8("gb_tableOwnership"));
        gb_tableOwnership->setFont(font5);
        gb_tableOwnership->setStyleSheet(QString::fromUtf8("QLineEdit\n"
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
"}"));
        verticalLayout_89 = new QVBoxLayout(gb_tableOwnership);
        verticalLayout_89->setObjectName(QString::fromUtf8("verticalLayout_89"));
        cb_tableOwnershipTableId = new QComboBox(gb_tableOwnership);
        cb_tableOwnershipTableId->setObjectName(QString::fromUtf8("cb_tableOwnershipTableId"));
        QSizePolicy sizePolicy13(QSizePolicy::Expanding, QSizePolicy::Fixed);
        sizePolicy13.setHorizontalStretch(0);
        sizePolicy13.setVerticalStretch(0);
        sizePolicy13.setHeightForWidth(cb_tableOwnershipTableId->sizePolicy().hasHeightForWidth());
        cb_tableOwnershipTableId->setSizePolicy(sizePolicy13);

        verticalLayout_89->addWidget(cb_tableOwnershipTableId);

        cb_tableOwnershipWorkerId = new QComboBox(gb_tableOwnership);
        cb_tableOwnershipWorkerId->setObjectName(QString::fromUtf8("cb_tableOwnershipWorkerId"));

        verticalLayout_89->addWidget(cb_tableOwnershipWorkerId);


        verticalLayout_88->addWidget(gb_tableOwnership);

        f_tableDbBtn_4 = new QFrame(f_tableOwnershipInput);
        f_tableDbBtn_4->setObjectName(QString::fromUtf8("f_tableDbBtn_4"));
        sizePolicy1.setHeightForWidth(f_tableDbBtn_4->sizePolicy().hasHeightForWidth());
        f_tableDbBtn_4->setSizePolicy(sizePolicy1);
        f_tableDbBtn_4->setFrameShape(QFrame::StyledPanel);
        f_tableDbBtn_4->setFrameShadow(QFrame::Raised);
        horizontalLayout_66 = new QHBoxLayout(f_tableDbBtn_4);
        horizontalLayout_66->setSpacing(5);
        horizontalLayout_66->setObjectName(QString::fromUtf8("horizontalLayout_66"));
        horizontalLayout_66->setContentsMargins(0, 0, 0, 0);
        btn_tableOwnershipAdd = new QPushButton(f_tableDbBtn_4);
        btn_tableOwnershipAdd->setObjectName(QString::fromUtf8("btn_tableOwnershipAdd"));
        btn_tableOwnershipAdd->setIcon(icon34);
        btn_tableOwnershipAdd->setIconSize(QSize(32, 32));

        horizontalLayout_66->addWidget(btn_tableOwnershipAdd);

        btn_tableOwnershipEdit = new QPushButton(f_tableDbBtn_4);
        btn_tableOwnershipEdit->setObjectName(QString::fromUtf8("btn_tableOwnershipEdit"));
        btn_tableOwnershipEdit->setEnabled(false);
        btn_tableOwnershipEdit->setIcon(icon35);
        btn_tableOwnershipEdit->setIconSize(QSize(32, 32));

        horizontalLayout_66->addWidget(btn_tableOwnershipEdit);

        btn_tableOwnershipDelete = new QPushButton(f_tableDbBtn_4);
        btn_tableOwnershipDelete->setObjectName(QString::fromUtf8("btn_tableOwnershipDelete"));
        btn_tableOwnershipDelete->setEnabled(false);
        btn_tableOwnershipDelete->setIcon(icon20);
        btn_tableOwnershipDelete->setIconSize(QSize(32, 32));

        horizontalLayout_66->addWidget(btn_tableOwnershipDelete);

        btn_tableOwnershipClear = new QPushButton(f_tableDbBtn_4);
        btn_tableOwnershipClear->setObjectName(QString::fromUtf8("btn_tableOwnershipClear"));
        btn_tableOwnershipClear->setEnabled(true);
        btn_tableOwnershipClear->setIcon(icon21);
        btn_tableOwnershipClear->setIconSize(QSize(32, 32));

        horizontalLayout_66->addWidget(btn_tableOwnershipClear);


        verticalLayout_88->addWidget(f_tableDbBtn_4);


        horizontalLayout_67->addWidget(f_tableOwnershipInput);

        f_tableOwnershipDb = new QFrame(tab_tableOwnership);
        f_tableOwnershipDb->setObjectName(QString::fromUtf8("f_tableOwnershipDb"));
        QSizePolicy sizePolicy14(QSizePolicy::Expanding, QSizePolicy::Preferred);
        sizePolicy14.setHorizontalStretch(0);
        sizePolicy14.setVerticalStretch(0);
        sizePolicy14.setHeightForWidth(f_tableOwnershipDb->sizePolicy().hasHeightForWidth());
        f_tableOwnershipDb->setSizePolicy(sizePolicy14);
        f_tableOwnershipDb->setFrameShape(QFrame::StyledPanel);
        f_tableOwnershipDb->setFrameShadow(QFrame::Raised);
        verticalLayout_87 = new QVBoxLayout(f_tableOwnershipDb);
        verticalLayout_87->setObjectName(QString::fromUtf8("verticalLayout_87"));
        tw_tableOwnershipDb = new QTableWidget(f_tableOwnershipDb);
        tw_tableOwnershipDb->setObjectName(QString::fromUtf8("tw_tableOwnershipDb"));
        tw_tableOwnershipDb->setFont(font8);
        tw_tableOwnershipDb->setEditTriggers(QAbstractItemView::NoEditTriggers);
        tw_tableOwnershipDb->setSelectionMode(QAbstractItemView::SingleSelection);
        tw_tableOwnershipDb->setSelectionBehavior(QAbstractItemView::SelectRows);
        tw_tableOwnershipDb->horizontalHeader()->setProperty("showSortIndicator", QVariant(true));
        tw_tableOwnershipDb->verticalHeader()->setCascadingSectionResizes(true);
        tw_tableOwnershipDb->verticalHeader()->setProperty("showSortIndicator", QVariant(false));

        verticalLayout_87->addWidget(tw_tableOwnershipDb);


        horizontalLayout_67->addWidget(f_tableOwnershipDb);

        QIcon icon53;
        icon53.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-package.svg"), QSize(), QIcon::Normal, QIcon::Off);
        tw_database->addTab(tab_tableOwnership, icon53, QString());

        gridLayout_9->addWidget(tw_database, 0, 0, 1, 1);

        sw_content->addWidget(page_database);
        page_workerStatus = new QWidget();
        page_workerStatus->setObjectName(QString::fromUtf8("page_workerStatus"));
        page_workerStatus->setStyleSheet(QString::fromUtf8("QPushButton\n"
"{ \n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"	padding: 2px;\n"
"	alternate-background-color: rgb(255, 255, 255);\n"
"	background: rgba(225, 225, 225, 100);\n"
"	border-width: 2px;\n"
"    border-radius: 10px;\n"
"	qproperty-iconSize: 50px 50px;\n"
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
"	background: rgba(225, 225, 225, 255);\n"
"	border-style: inset;\n"
"}\n"
"\n"
"QLabel\n"
"{\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"	alignment: \"center\"\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"	font: 12pt \"MS Shell Dlg 2\";\n"
"	alignment: \"center\";\n"
"	background: rgba(225, 225, 225, 200);\n"
"}"));
        gridLayout_20 = new QGridLayout(page_workerStatus);
        gridLayout_20->setObjectName(QString::fromUtf8("gridLayout_20"));
        sa_workerStatus = new QScrollArea(page_workerStatus);
        sa_workerStatus->setObjectName(QString::fromUtf8("sa_workerStatus"));
        sa_workerStatus->setStyleSheet(QString::fromUtf8("QLineEdit\n"
"{\n"
"	background: transparent;\n"
"	color: rgb(88, 88, 88);\n"
"	border: none;\n"
"	border-bottom: 1px solid #717072;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}\n"
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
""));
        sa_workerStatus->setWidgetResizable(true);
        w_workerStats = new QWidget();
        w_workerStats->setObjectName(QString::fromUtf8("w_workerStats"));
        w_workerStats->setGeometry(QRect(0, 0, 411, 175));
        gridLayout_21 = new QGridLayout(w_workerStats);
        gridLayout_21->setObjectName(QString::fromUtf8("gridLayout_21"));
        frame_13 = new QFrame(w_workerStats);
        frame_13->setObjectName(QString::fromUtf8("frame_13"));
        frame_13->setMaximumSize(QSize(200, 200));
        frame_13->setFrameShape(QFrame::Box);
        frame_13->setFrameShadow(QFrame::Plain);
        verticalLayout_78 = new QVBoxLayout(frame_13);
        verticalLayout_78->setObjectName(QString::fromUtf8("verticalLayout_78"));
        label_30 = new QLabel(frame_13);
        label_30->setObjectName(QString::fromUtf8("label_30"));
        label_30->setAlignment(Qt::AlignCenter);

        verticalLayout_78->addWidget(label_30);

        textEdit = new QTextEdit(frame_13);
        textEdit->setObjectName(QString::fromUtf8("textEdit"));

        verticalLayout_78->addWidget(textEdit);

        frame_291 = new QFrame(frame_13);
        frame_291->setObjectName(QString::fromUtf8("frame_291"));
        frame_291->setMaximumSize(QSize(200, 100));
        frame_291->setFrameShape(QFrame::StyledPanel);
        frame_291->setFrameShadow(QFrame::Raised);
        horizontalLayout_55 = new QHBoxLayout(frame_291);
        horizontalLayout_55->setSpacing(5);
        horizontalLayout_55->setObjectName(QString::fromUtf8("horizontalLayout_55"));
        horizontalLayout_55->setContentsMargins(0, 0, 0, 0);
        pushButton_52 = new QPushButton(frame_291);
        pushButton_52->setObjectName(QString::fromUtf8("pushButton_52"));

        horizontalLayout_55->addWidget(pushButton_52);

        pushButton_53 = new QPushButton(frame_291);
        pushButton_53->setObjectName(QString::fromUtf8("pushButton_53"));

        horizontalLayout_55->addWidget(pushButton_53);


        verticalLayout_78->addWidget(frame_291);


        gridLayout_21->addWidget(frame_13, 0, 0, 1, 1);

        frame_43 = new QFrame(w_workerStats);
        frame_43->setObjectName(QString::fromUtf8("frame_43"));
        frame_43->setMaximumSize(QSize(200, 200));
        frame_43->setFrameShape(QFrame::Box);
        frame_43->setFrameShadow(QFrame::Plain);
        verticalLayout_93 = new QVBoxLayout(frame_43);
        verticalLayout_93->setObjectName(QString::fromUtf8("verticalLayout_93"));
        label_42 = new QLabel(frame_43);
        label_42->setObjectName(QString::fromUtf8("label_42"));
        label_42->setAlignment(Qt::AlignCenter);

        verticalLayout_93->addWidget(label_42);

        textEdit_2 = new QTextEdit(frame_43);
        textEdit_2->setObjectName(QString::fromUtf8("textEdit_2"));

        verticalLayout_93->addWidget(textEdit_2);

        frame_45 = new QFrame(frame_43);
        frame_45->setObjectName(QString::fromUtf8("frame_45"));
        frame_45->setMaximumSize(QSize(200, 100));
        frame_45->setFrameShape(QFrame::StyledPanel);
        frame_45->setFrameShadow(QFrame::Raised);
        horizontalLayout_70 = new QHBoxLayout(frame_45);
        horizontalLayout_70->setSpacing(5);
        horizontalLayout_70->setObjectName(QString::fromUtf8("horizontalLayout_70"));
        horizontalLayout_70->setContentsMargins(0, 0, 0, 0);
        pushButton_66 = new QPushButton(frame_45);
        pushButton_66->setObjectName(QString::fromUtf8("pushButton_66"));

        horizontalLayout_70->addWidget(pushButton_66);

        pushButton_67 = new QPushButton(frame_45);
        pushButton_67->setObjectName(QString::fromUtf8("pushButton_67"));

        horizontalLayout_70->addWidget(pushButton_67);


        verticalLayout_93->addWidget(frame_45);


        gridLayout_21->addWidget(frame_43, 0, 1, 1, 1);

        frame_46 = new QFrame(w_workerStats);
        frame_46->setObjectName(QString::fromUtf8("frame_46"));
        frame_46->setMaximumSize(QSize(200, 200));
        frame_46->setFrameShape(QFrame::Box);
        frame_46->setFrameShadow(QFrame::Plain);
        verticalLayout_94 = new QVBoxLayout(frame_46);
        verticalLayout_94->setObjectName(QString::fromUtf8("verticalLayout_94"));
        label_43 = new QLabel(frame_46);
        label_43->setObjectName(QString::fromUtf8("label_43"));
        label_43->setAlignment(Qt::AlignCenter);

        verticalLayout_94->addWidget(label_43);

        textEdit_3 = new QTextEdit(frame_46);
        textEdit_3->setObjectName(QString::fromUtf8("textEdit_3"));

        verticalLayout_94->addWidget(textEdit_3);

        frame_47 = new QFrame(frame_46);
        frame_47->setObjectName(QString::fromUtf8("frame_47"));
        frame_47->setMaximumSize(QSize(200, 100));
        frame_47->setFrameShape(QFrame::StyledPanel);
        frame_47->setFrameShadow(QFrame::Raised);
        horizontalLayout_71 = new QHBoxLayout(frame_47);
        horizontalLayout_71->setSpacing(5);
        horizontalLayout_71->setObjectName(QString::fromUtf8("horizontalLayout_71"));
        horizontalLayout_71->setContentsMargins(0, 0, 0, 0);
        pushButton_68 = new QPushButton(frame_47);
        pushButton_68->setObjectName(QString::fromUtf8("pushButton_68"));

        horizontalLayout_71->addWidget(pushButton_68);

        pushButton_69 = new QPushButton(frame_47);
        pushButton_69->setObjectName(QString::fromUtf8("pushButton_69"));

        horizontalLayout_71->addWidget(pushButton_69);


        verticalLayout_94->addWidget(frame_47);


        gridLayout_21->addWidget(frame_46, 0, 2, 1, 1);

        sa_workerStatus->setWidget(w_workerStats);

        gridLayout_20->addWidget(sa_workerStatus, 0, 0, 1, 1);

        sw_content->addWidget(page_workerStatus);
        page_stats = new QWidget();
        page_stats->setObjectName(QString::fromUtf8("page_stats"));
        page_stats->setStyleSheet(QString::fromUtf8(""));
        gridLayout_18 = new QGridLayout(page_stats);
        gridLayout_18->setObjectName(QString::fromUtf8("gridLayout_18"));
        sw_content->addWidget(page_stats);

        verticalLayout_16->addWidget(sw_content);


        verticalLayout_3->addWidget(f_content);

        f_footer = new QFrame(f_body);
        f_footer->setObjectName(QString::fromUtf8("f_footer"));
        f_footer->setMinimumSize(QSize(0, 20));
        f_footer->setMaximumSize(QSize(16777215, 40));
        f_footer->setTabletTracking(false);
        f_footer->setStyleSheet(QString::fromUtf8("#f_footer{\n"
"	background-color: qlineargradient(spread:reflect, x1:0.512, y1:1, x2:1, y2:0.994, stop:0 rgba(190, 190, 190, 200), stop:1 rgba(131, 131, 131, 20));\n"
"}\n"
"\n"
"\n"
"QPushButton\n"
"{ \n"
"	alternate-background-color: rgb(255, 255, 255);\n"
"	background: rgba(225, 225, 225, 0);\n"
"	border-width: 0px;\n"
"    border-radius: 0px;\n"
"	qproperty-iconSize: 16px 16px;\n"
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
"}"));
        f_footer->setFrameShape(QFrame::StyledPanel);
        f_footer->setFrameShadow(QFrame::Raised);
        horizontalLayout_2 = new QHBoxLayout(f_footer);
        horizontalLayout_2->setSpacing(0);
        horizontalLayout_2->setObjectName(QString::fromUtf8("horizontalLayout_2"));
        horizontalLayout_2->setContentsMargins(0, 0, 0, 0);
        l_version = new QLabel(f_footer);
        l_version->setObjectName(QString::fromUtf8("l_version"));
        l_version->setFont(font1);
        l_version->setTabletTracking(false);
        l_version->setAlignment(Qt::AlignCenter);

        horizontalLayout_2->addWidget(l_version);

        l_serverStatus = new QLabel(f_footer);
        l_serverStatus->setObjectName(QString::fromUtf8("l_serverStatus"));
        l_serverStatus->setFont(font1);
        l_serverStatus->setTabletTracking(false);
        l_serverStatus->setAlignment(Qt::AlignCenter);

        horizontalLayout_2->addWidget(l_serverStatus);

        l_creator = new QLabel(f_footer);
        l_creator->setObjectName(QString::fromUtf8("l_creator"));
        l_creator->setFont(font1);
        l_creator->setTabletTracking(false);
        l_creator->setAlignment(Qt::AlignCenter);

        horizontalLayout_2->addWidget(l_creator);

        btn_logs = new QPushButton(f_footer);
        btn_logs->setObjectName(QString::fromUtf8("btn_logs"));
        btn_logs->setEnabled(false);
        sizePolicy4.setHeightForWidth(btn_logs->sizePolicy().hasHeightForWidth());
        btn_logs->setSizePolicy(sizePolicy4);
        btn_logs->setMaximumSize(QSize(20, 16777215));
        QIcon icon54;
        icon54.addFile(QString::fromUtf8(":/Simple icons/simple_icons/fi-rr-shield-interrogation.svg"), QSize(), QIcon::Normal, QIcon::Off);
        btn_logs->setIcon(icon54);
        btn_logs->setIconSize(QSize(16, 16));

        horizontalLayout_2->addWidget(btn_logs);


        verticalLayout_3->addWidget(f_footer, 0, Qt::AlignBottom);


        horizontalLayout->addWidget(f_body);

        f_notification = new QFrame(f_main);
        f_notification->setObjectName(QString::fromUtf8("f_notification"));
        f_notification->setMinimumSize(QSize(400, 0));
        f_notification->setMaximumSize(QSize(500, 16777215));
        f_notification->setFrameShape(QFrame::StyledPanel);
        f_notification->setFrameShadow(QFrame::Raised);
        verticalLayout_84 = new QVBoxLayout(f_notification);
        verticalLayout_84->setObjectName(QString::fromUtf8("verticalLayout_84"));
        scrollArea = new QScrollArea(f_notification);
        scrollArea->setObjectName(QString::fromUtf8("scrollArea"));
        scrollArea->setFrameShape(QFrame::WinPanel);
        scrollArea->setFrameShadow(QFrame::Plain);
        scrollArea->setWidgetResizable(true);
        scrollArea->setAlignment(Qt::AlignCenter);
        scrollAreaWidgetContents = new QWidget();
        scrollAreaWidgetContents->setObjectName(QString::fromUtf8("scrollAreaWidgetContents"));
        scrollAreaWidgetContents->setGeometry(QRect(0, 0, 376, 748));
        verticalLayout_85 = new QVBoxLayout(scrollAreaWidgetContents);
        verticalLayout_85->setObjectName(QString::fromUtf8("verticalLayout_85"));
        w_notification = new QWidget(scrollAreaWidgetContents);
        w_notification->setObjectName(QString::fromUtf8("w_notification"));
        w_notification->setStyleSheet(QString::fromUtf8("*\n"
"{\n"
"	font: 14pt \"Times New Roman\";\n"
"}"));
        verticalLayout_86 = new QVBoxLayout(w_notification);
        verticalLayout_86->setObjectName(QString::fromUtf8("verticalLayout_86"));

        verticalLayout_85->addWidget(w_notification);

        scrollArea->setWidget(scrollAreaWidgetContents);

        verticalLayout_84->addWidget(scrollArea);

        btn_notification_clear = new QPushButton(f_notification);
        btn_notification_clear->setObjectName(QString::fromUtf8("btn_notification_clear"));
        btn_notification_clear->setFont(font5);
        btn_notification_clear->setIcon(icon21);

        verticalLayout_84->addWidget(btn_notification_clear);


        horizontalLayout->addWidget(f_notification);


        verticalLayout->addWidget(f_main);

        PatusMainWindow->setCentralWidget(w_background);

        retranslateUi(PatusMainWindow);
        QObject::connect(cb_reservationDate, &QCheckBox::clicked, de_reservationSearchDate, &QDateEdit::setEnabled);
        QObject::connect(btn_productReceiptClear, &QPushButton::clicked, le_productReceiptIngredientQuantity, qOverload<>(&QLineEdit::clear));

        sw_content->setCurrentIndex(0);
        tw_foodMenu->setCurrentIndex(0);
        tw_database->setCurrentIndex(0);
        cb_menuItemCategory->setCurrentIndex(0);


        QMetaObject::connectSlotsByName(PatusMainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *PatusMainWindow)
    {
        PatusMainWindow->setWindowTitle(QCoreApplication::translate("PatusMainWindow", "Patus", nullptr));
        btn_logInOut->setText(QString());
        btn_tables->setText(QString());
        btn_cashRegister->setText(QString());
        btn_reservation->setText(QString());
        btn_waste->setText(QString());
        btn_databaseOverview->setText(QString());
        btn_productReceipt->setText(QString());
        btn_database->setText(QString());
        btn_workerStatus->setText(QString());
        btn_statistic->setText(QString());
        btn_exit->setText(QString());
        btn_sideBar->setText(QString());
        l_busyTables->setText(QCoreApplication::translate("PatusMainWindow", "Busy tables: 8", nullptr));
        l_monthSells->setText(QCoreApplication::translate("PatusMainWindow", "Total day sells: 0", nullptr));
        l_freeTables->setText(QCoreApplication::translate("PatusMainWindow", "Free tables: 12", nullptr));
        l_daySells->setText(QCoreApplication::translate("PatusMainWindow", "Total month sells: 0", nullptr));
        btn_blockNote->setText(QString());
        btn_notification->setText(QString());
        btn_setting->setText(QString());
        btn_fullScreen->setText(QString());
        l_date->setText(QCoreApplication::translate("PatusMainWindow", "2021-08-24", nullptr));
        l_time->setText(QCoreApplication::translate("PatusMainWindow", "20:00:00", nullptr));
        l_welcomeMsg->setText(QCoreApplication::translate("PatusMainWindow", "Welcome to Patus", nullptr));
        btn_biometric->setText(QString());
        le_username->setText(QString());
        le_username->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Username", nullptr));
        le_password->setText(QString());
        le_password->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Password", nullptr));
        btn_loginConfirm->setText(QCoreApplication::translate("PatusMainWindow", "Login", nullptr));
#if QT_CONFIG(shortcut)
        btn_loginConfirm->setShortcut(QCoreApplication::translate("PatusMainWindow", "Return", nullptr));
#endif // QT_CONFIG(shortcut)
        l_cashRegisterTicketNumberTitle->setText(QCoreApplication::translate("PatusMainWindow", "Ticket Number", nullptr));
        l_cashRegisterTicketNumber->setText(QCoreApplication::translate("PatusMainWindow", "-", nullptr));
        l_cashRegisterTableNumberTitle->setText(QCoreApplication::translate("PatusMainWindow", "Table Number", nullptr));
        l_cashRegisterTableNumber->setText(QCoreApplication::translate("PatusMainWindow", "-", nullptr));
        btn_cashRegisterChangeTable->setText(QString());
        rb_takeAway->setText(QCoreApplication::translate("PatusMainWindow", "Take away", nullptr));
        rb_onTable->setText(QCoreApplication::translate("PatusMainWindow", "On table", nullptr));
        btn_cashRegisterDeleteCurrent->setText(QString());
        btn_cashRegisterClear->setText(QString());
        btn_cashRegisterResume->setText(QString());
        btn_cashRegisterHold->setText(QString());
        l_taxDa->setText(QCoreApplication::translate("PatusMainWindow", "DA", nullptr));
        l_totalTtc->setText(QCoreApplication::translate("PatusMainWindow", "Final Total", nullptr));
        l_da->setText(QCoreApplication::translate("PatusMainWindow", "DA", nullptr));
        l_totalHtt->setText(QCoreApplication::translate("PatusMainWindow", "Total", nullptr));
        l_tax->setText(QCoreApplication::translate("PatusMainWindow", "Reduction", nullptr));
        l_TtcDa->setText(QCoreApplication::translate("PatusMainWindow", "DA", nullptr));
        btn_cashRegisterReduce->setText(QString());
        btn_cashRegisterTicketKitchen->setText(QString());
        btn_cashRegisterTicket->setText(QString());
        btn_cashRegisterPay->setText(QString());
        l_orderWorker->setText(QCoreApplication::translate("PatusMainWindow", "Worker name", nullptr));
        l_orderCustomer->setText(QCoreApplication::translate("PatusMainWindow", "Customer name", nullptr));
        groupBox_2->setTitle(QCoreApplication::translate("PatusMainWindow", "Comment", nullptr));
        label_15->setText(QString());
        label_16->setText(QCoreApplication::translate("PatusMainWindow", "Burger", nullptr));
        pushButton_38->setText(QCoreApplication::translate("PatusMainWindow", "+", nullptr));
        pushButton_39->setText(QCoreApplication::translate("PatusMainWindow", "-", nullptr));
        label_17->setText(QString());
        label_18->setText(QCoreApplication::translate("PatusMainWindow", "Burger", nullptr));
        pushButton_40->setText(QCoreApplication::translate("PatusMainWindow", "+", nullptr));
        pushButton_41->setText(QCoreApplication::translate("PatusMainWindow", "-", nullptr));
        label_32->setText(QString());
        label_33->setText(QCoreApplication::translate("PatusMainWindow", "Burger", nullptr));
        pushButton_56->setText(QCoreApplication::translate("PatusMainWindow", "+", nullptr));
        pushButton_57->setText(QCoreApplication::translate("PatusMainWindow", "-", nullptr));
        tw_foodMenu->setTabText(tw_foodMenu->indexOf(tab_salade), QString());
        label_19->setText(QString());
        label_20->setText(QCoreApplication::translate("PatusMainWindow", "Burger", nullptr));
        pushButton_42->setText(QCoreApplication::translate("PatusMainWindow", "+", nullptr));
        pushButton_43->setText(QCoreApplication::translate("PatusMainWindow", "-", nullptr));
        label_21->setText(QString());
        label_22->setText(QCoreApplication::translate("PatusMainWindow", "Burger", nullptr));
        pushButton_44->setText(QCoreApplication::translate("PatusMainWindow", "+", nullptr));
        pushButton_45->setText(QCoreApplication::translate("PatusMainWindow", "-", nullptr));
        label_29->setText(QString());
        label_31->setText(QCoreApplication::translate("PatusMainWindow", "Burger", nullptr));
        pushButton_54->setText(QCoreApplication::translate("PatusMainWindow", "+", nullptr));
        pushButton_55->setText(QCoreApplication::translate("PatusMainWindow", "-", nullptr));
        tw_foodMenu->setTabText(tw_foodMenu->indexOf(tab_meal), QString());
        label->setText(QString());
        label_5->setText(QCoreApplication::translate("PatusMainWindow", "Burger", nullptr));
        pushButton_4->setText(QCoreApplication::translate("PatusMainWindow", "+", nullptr));
        pushButton_14->setText(QCoreApplication::translate("PatusMainWindow", "-", nullptr));
        label_2->setText(QString());
        label_6->setText(QCoreApplication::translate("PatusMainWindow", "Burger", nullptr));
        pushButton_15->setText(QCoreApplication::translate("PatusMainWindow", "+", nullptr));
        pushButton_16->setText(QCoreApplication::translate("PatusMainWindow", "-", nullptr));
        label_3->setText(QString());
        label_7->setText(QCoreApplication::translate("PatusMainWindow", "Burger", nullptr));
        pushButton_17->setText(QCoreApplication::translate("PatusMainWindow", "+", nullptr));
        pushButton_18->setText(QCoreApplication::translate("PatusMainWindow", "-", nullptr));
        tw_foodMenu->setTabText(tw_foodMenu->indexOf(tab_pizza), QString());
        label_25->setText(QString());
        label_26->setText(QCoreApplication::translate("PatusMainWindow", "Burger", nullptr));
        pushButton_48->setText(QCoreApplication::translate("PatusMainWindow", "+", nullptr));
        pushButton_49->setText(QCoreApplication::translate("PatusMainWindow", "-", nullptr));
        label_23->setText(QString());
        label_24->setText(QCoreApplication::translate("PatusMainWindow", "Burger", nullptr));
        pushButton_46->setText(QCoreApplication::translate("PatusMainWindow", "+", nullptr));
        pushButton_47->setText(QCoreApplication::translate("PatusMainWindow", "-", nullptr));
        label_34->setText(QString());
        label_41->setText(QCoreApplication::translate("PatusMainWindow", "Burger", nullptr));
        pushButton_64->setText(QCoreApplication::translate("PatusMainWindow", "+", nullptr));
        pushButton_65->setText(QCoreApplication::translate("PatusMainWindow", "-", nullptr));
        tw_foodMenu->setTabText(tw_foodMenu->indexOf(tab_coldDrink), QString());
        label_35->setText(QString());
        label_36->setText(QCoreApplication::translate("PatusMainWindow", "Burger", nullptr));
        pushButton_58->setText(QCoreApplication::translate("PatusMainWindow", "+", nullptr));
        pushButton_59->setText(QCoreApplication::translate("PatusMainWindow", "-", nullptr));
        label_27->setText(QString());
        label_28->setText(QCoreApplication::translate("PatusMainWindow", "Burger", nullptr));
        pushButton_50->setText(QCoreApplication::translate("PatusMainWindow", "+", nullptr));
        pushButton_51->setText(QCoreApplication::translate("PatusMainWindow", "-", nullptr));
        label_44->setText(QString());
        label_45->setText(QCoreApplication::translate("PatusMainWindow", "Burger", nullptr));
        pushButton_70->setText(QCoreApplication::translate("PatusMainWindow", "+", nullptr));
        pushButton_71->setText(QCoreApplication::translate("PatusMainWindow", "-", nullptr));
        tw_foodMenu->setTabText(tw_foodMenu->indexOf(tab_hotDrink), QString());
        label_39->setText(QString());
        label_40->setText(QCoreApplication::translate("PatusMainWindow", "Burger", nullptr));
        pushButton_62->setText(QCoreApplication::translate("PatusMainWindow", "+", nullptr));
        pushButton_63->setText(QCoreApplication::translate("PatusMainWindow", "-", nullptr));
        label_37->setText(QString());
        label_38->setText(QCoreApplication::translate("PatusMainWindow", "Burger", nullptr));
        comboBox->setItemText(0, QCoreApplication::translate("PatusMainWindow", "1", nullptr));
        comboBox->setItemText(1, QCoreApplication::translate("PatusMainWindow", "2", nullptr));
        comboBox->setItemText(2, QCoreApplication::translate("PatusMainWindow", "3", nullptr));
        comboBox->setItemText(3, QCoreApplication::translate("PatusMainWindow", "4", nullptr));

        pushButton_60->setText(QCoreApplication::translate("PatusMainWindow", "+", nullptr));
        pushButton_61->setText(QCoreApplication::translate("PatusMainWindow", "-", nullptr));
        label_46->setText(QString());
        label_47->setText(QCoreApplication::translate("PatusMainWindow", "Burger", nullptr));
        pushButton_72->setText(QCoreApplication::translate("PatusMainWindow", "+", nullptr));
        pushButton_73->setText(QCoreApplication::translate("PatusMainWindow", "-", nullptr));
        tw_foodMenu->setTabText(tw_foodMenu->indexOf(tab_dessert), QString());
        gb_reservation->setTitle(QCoreApplication::translate("PatusMainWindow", "Reservation", nullptr));
        le_reservationName->setText(QString());
        le_reservationName->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Name", nullptr));
        le_reservationPhone->setText(QString());
        le_reservationPhone->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Phone", nullptr));
        le_reservationNbPerson->setText(QString());
        le_reservationNbPerson->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Number of person", nullptr));
        dte_reservation->setDisplayFormat(QCoreApplication::translate("PatusMainWindow", "yyyy-MM-dd HH:mm", nullptr));
        btn_reservationAdd->setText(QString());
        btn_reservationEdit->setText(QString());
        btn_reservationDelete->setText(QString());
        btn_reservationClear->setText(QString());
        cb_reservationSearchType->setItemText(0, QCoreApplication::translate("PatusMainWindow", "Name", nullptr));
        cb_reservationSearchType->setItemText(1, QCoreApplication::translate("PatusMainWindow", "Phone", nullptr));

        le_reservationSearch->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Search", nullptr));
        btn_reservationSearch->setText(QString());
        cb_reservationDate->setText(QCoreApplication::translate("PatusMainWindow", "Use date", nullptr));
        de_reservationSearchDate->setDisplayFormat(QCoreApplication::translate("PatusMainWindow", "yyyy-MM-dd", nullptr));
        groupBox_4->setTitle(QCoreApplication::translate("PatusMainWindow", "Waste from Stock", nullptr));
        le_wasteStockQuantity->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Quantity", nullptr));
        btn_wasteStockClear->setText(QString());
        btn_wasteStockSave->setText(QString());
        groupBox_3->setTitle(QCoreApplication::translate("PatusMainWindow", "Other Waste", nullptr));
        le_wasteCustomName->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Name", nullptr));
        le_wasteCustomQuantity->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Quantity", nullptr));
        le_wasteCustomPrice->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Price", nullptr));
        btn_wasteCustomClear->setText(QString());
        btn_wasteCustomSave->setText(QString());
        l_stock->setText(QCoreApplication::translate("PatusMainWindow", "Stock", nullptr));
        rb_stockIngredients->setText(QCoreApplication::translate("PatusMainWindow", "Ingredients", nullptr));
        rb_stockOthers->setText(QCoreApplication::translate("PatusMainWindow", "Others", nullptr));
        l_productReceiptSelection->setText(QCoreApplication::translate("PatusMainWindow", "Menu Item Receipt", nullptr));
        l_ingredient_2->setText(QCoreApplication::translate("PatusMainWindow", "Menu Item", nullptr));
        btn_productReceiptAdd->setText(QString());
        btn_productReceiptRemove->setText(QString());
        le_productReceiptIngredientQuantity->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Quantity", nullptr));
        btn_productReceiptEdit->setText(QString());
        l_ingredient->setText(QCoreApplication::translate("PatusMainWindow", "Ingredient", nullptr));
        btn_productReceiptClear->setText(QString());
        l_ingredient_7->setText(QCoreApplication::translate("PatusMainWindow", "Sell price", nullptr));
        l_ingredient_5->setText(QCoreApplication::translate("PatusMainWindow", "Estimated production price", nullptr));
        l_ingredient_8->setText(QCoreApplication::translate("PatusMainWindow", "Estimated quantity", nullptr));
        l_productReceiptQuantity->setText(QCoreApplication::translate("PatusMainWindow", "0", nullptr));
        l_productReceiptPrice->setText(QCoreApplication::translate("PatusMainWindow", "0", nullptr));
        l_productReceiptEstimatedProductionPrice->setText(QCoreApplication::translate("PatusMainWindow", "0", nullptr));
        gb_menuItem->setTitle(QCoreApplication::translate("PatusMainWindow", "Menu Item", nullptr));
        l_menuItemPicture->setText(QString());
        btn_menuItemPicture->setText(QString());
        btn_menuItemPictureClear->setText(QString());
        le_menuItemName->setText(QString());
        le_menuItemName->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Name", nullptr));
        cb_menuItemCategory->setItemText(0, QCoreApplication::translate("PatusMainWindow", "Salade", nullptr));
        cb_menuItemCategory->setItemText(1, QCoreApplication::translate("PatusMainWindow", "Meal", nullptr));
        cb_menuItemCategory->setItemText(2, QCoreApplication::translate("PatusMainWindow", "Pizza", nullptr));
        cb_menuItemCategory->setItemText(3, QCoreApplication::translate("PatusMainWindow", "Cold Drink", nullptr));
        cb_menuItemCategory->setItemText(4, QCoreApplication::translate("PatusMainWindow", "Hot Drink", nullptr));
        cb_menuItemCategory->setItemText(5, QCoreApplication::translate("PatusMainWindow", "Dessert", nullptr));

        le_menuItemUnit->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Unit", nullptr));
        le_menuItemUnitQuantity->setText(QString());
        le_menuItemUnitQuantity->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Unit Quantity", nullptr));
        le_menuItemPrice->setText(QString());
        le_menuItemPrice->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Unit Price", nullptr));
        btn_menuItemAdd->setText(QString());
        btn_menuItemEdit->setText(QString());
        btn_menuItemDelete->setText(QString());
        btn_menuItemClear->setText(QString());
        tw_database->setTabText(tw_database->indexOf(tab_menu), QString());
        gb_menuCategoryCustom->setTitle(QCoreApplication::translate("PatusMainWindow", "Menu Category", nullptr));
        le_menuCategoryCustomName->setText(QString());
        le_menuCategoryCustomName->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Name", nullptr));
        cb_menuCategoryCustomPrinting->setItemText(0, QCoreApplication::translate("PatusMainWindow", "Kitchen", nullptr));
        cb_menuCategoryCustomPrinting->setItemText(1, QCoreApplication::translate("PatusMainWindow", "Pizza Yolo", nullptr));
        cb_menuCategoryCustomPrinting->setItemText(2, QCoreApplication::translate("PatusMainWindow", "Bar", nullptr));

        btn_menuCategoryCustomAdd->setText(QString());
        btn_menuCategoryCustomEdit->setText(QString());
        btn_menuCategoryCustomDelete->setText(QString());
        btn_menuCategoryCustomClear->setText(QString());
        tw_database->setTabText(tw_database->indexOf(tab), QString());
        gb_supplement->setTitle(QCoreApplication::translate("PatusMainWindow", "Supplement", nullptr));
        le_supplementName->setText(QString());
        le_supplementName->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Name", nullptr));
        le_supplementQuantity->setText(QString());
        le_supplementQuantity->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Quantity", nullptr));
        le_supplementPrice->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Price", nullptr));
        btn_supplementAdd->setText(QString());
        btn_supplementEdit->setText(QString());
        btn_supplementDelete->setText(QString());
        btn_supplementClear->setText(QString());
        tw_database->setTabText(tw_database->indexOf(tab_supplement), QString());
        gb_expense->setTitle(QCoreApplication::translate("PatusMainWindow", "Expense", nullptr));
        le_expenseName->setText(QString());
        le_expenseName->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Name", nullptr));
        le_expenseUnit->setText(QString());
        le_expenseUnit->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Unit", nullptr));
        le_expenseQuantity->setText(QString());
        le_expenseQuantity->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Quantity", nullptr));
        le_expensePrice->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Total price", nullptr));
        cb_expenseSupplier->setItemText(0, QCoreApplication::translate("PatusMainWindow", "None", nullptr));

        cb_expensePayed->setText(QCoreApplication::translate("PatusMainWindow", "Is payed ?", nullptr));
        btn_expenseAdd->setText(QString());
        btn_expenseEdit->setText(QString());
        btn_expenseDelete->setText(QString());
        btn_expenseClear->setText(QString());
        tw_database->setTabText(tw_database->indexOf(tab_expense), QString());
        gb_expenseCategory->setTitle(QCoreApplication::translate("PatusMainWindow", "Expense Category", nullptr));
        le_expenseCategoryName->setText(QString());
        le_expenseCategoryName->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Name", nullptr));
        cb_expenseCategorySaveToStock->setText(QCoreApplication::translate("PatusMainWindow", "Save to stock ?", nullptr));
        cb_expenseCategoryIsIngredient->setText(QCoreApplication::translate("PatusMainWindow", "Is ingredient ?", nullptr));
        btn_expenseCategoryAdd->setText(QString());
        btn_expenseCategoryEdit->setText(QString());
        btn_expenseCategoryDelete->setText(QString());
        btn_expenseCategoryClear->setText(QString());
        tw_database->setTabText(tw_database->indexOf(tab_expenseCategory), QString());
        gb_supplier->setTitle(QCoreApplication::translate("PatusMainWindow", "Supplier", nullptr));
        le_supplierName->setText(QString());
        le_supplierName->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Name", nullptr));
        le_supplierPhone->setText(QString());
        le_supplierPhone->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Phone", nullptr));
        le_supplierAddress->setText(QString());
        le_supplierAddress->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Address", nullptr));
        le_supplierMail->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Mail", nullptr));
        btn_supplierAdd->setText(QString());
        btn_supplierEdit->setText(QString());
        btn_supplierDelete->setText(QString());
        btn_supplierClear->setText(QString());
        tw_database->setTabText(tw_database->indexOf(tab_supplier), QString());
        gb_customer->setTitle(QCoreApplication::translate("PatusMainWindow", "Customer", nullptr));
        l_customerPicture->setText(QString());
        btn_customerPicture->setText(QString());
        btn_customerPictureClear->setText(QString());
        le_customerName->setText(QString());
        le_customerName->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "First and Last Name", nullptr));
        le_customerPhone->setText(QString());
        le_customerPhone->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Phone", nullptr));
        le_customerAddress->setText(QString());
        le_customerAddress->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Address", nullptr));
        le_customerScore->setInputMask(QString());
        le_customerScore->setText(QString());
        le_customerScore->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Score", nullptr));
        btn_customerAdd->setText(QString());
        btn_customerEdit->setText(QString());
        btn_customerDelete->setText(QString());
        btn_customerClear->setText(QString());
        tw_database->setTabText(tw_database->indexOf(tab_customer), QString());
        gb_worker->setTitle(QCoreApplication::translate("PatusMainWindow", "Worker", nullptr));
        l_workerPicture->setText(QString());
        btn_workerPicture->setText(QString());
        btn_workerPictureClear->setText(QString());
        le_workerName->setText(QString());
        le_workerName->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "First and Last Name", nullptr));
        le_workerUsername->setText(QString());
        le_workerUsername->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Username", nullptr));
        le_workerPassword->setText(QString());
        le_workerPassword->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Password", nullptr));
        le_workerPhone->setText(QString());
        le_workerPhone->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Phone", nullptr));
        le_workerAddress->setText(QString());
        le_workerAddress->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Address", nullptr));
        le_workerSalary->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Salary", nullptr));
        le_workerScore->setText(QString());
        le_workerScore->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Score", nullptr));
        le_workerCv->setText(QString());
        le_workerCv->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "CV extension", nullptr));
        btn_workerAddCv->setText(QString());
        btn_workerOpenCv->setText(QString());
        btn_workerClearCv->setText(QString());
        btn_workerAdd->setText(QString());
        btn_workerEdit->setText(QString());
        btn_workerDelete->setText(QString());
        btn_workerClear->setText(QString());
        tw_database->setTabText(tw_database->indexOf(tab_worker), QString());
        gb_category->setTitle(QCoreApplication::translate("PatusMainWindow", "Worker Category", nullptr));
        le_categoryName->setText(QString());
        le_categoryName->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Name", nullptr));
        cb_categoryLevelCashier->setText(QCoreApplication::translate("PatusMainWindow", "Cashier", nullptr));
        cb_categoryLevelWaste->setText(QCoreApplication::translate("PatusMainWindow", "Waste", nullptr));
        cb_categoryLevelTables->setText(QCoreApplication::translate("PatusMainWindow", "Tables", nullptr));
        cb_categoryLevelStock->setText(QCoreApplication::translate("PatusMainWindow", "Stock", nullptr));
        cb_categoryLevelReservation->setText(QCoreApplication::translate("PatusMainWindow", "Reservation", nullptr));
        cb_categoryLevelReceipt->setText(QCoreApplication::translate("PatusMainWindow", "Receipt", nullptr));
        cb_categoryLevelDb->setText(QCoreApplication::translate("PatusMainWindow", "DataBase", nullptr));
        cb_categoryLevelPhone->setText(QCoreApplication::translate("PatusMainWindow", "Phones", nullptr));
        cb_categoryLevelStat->setText(QCoreApplication::translate("PatusMainWindow", "DashBoard", nullptr));
        btn_categoryAdd->setText(QString());
        btn_categoryEdit->setText(QString());
        btn_categoryDelete->setText(QString());
        btn_categoryClear->setText(QString());
        tw_database->setTabText(tw_database->indexOf(tab_category), QString());
        gb_sell->setTitle(QCoreApplication::translate("PatusMainWindow", "Sell", nullptr));
        dte_sellDate->setDisplayFormat(QCoreApplication::translate("PatusMainWindow", "yyyy-MM-dd HH:mm:ss", nullptr));
        le_sellTotal->setText(QString());
        le_sellTotal->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Total", nullptr));
        le_sellNbCovers->setText(QString());
        le_sellNbCovers->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Number of covers", nullptr));
        btn_sellAdd->setText(QString());
        btn_sellEdit->setText(QString());
        btn_sellDelete->setText(QString());
        btn_sellClear->setText(QString());
        btn_sellShow->setText(QString());
        btn_sellLoad->setText(QString());
        tw_database->setTabText(tw_database->indexOf(tab_sell), QString());
        gb_expense_6->setTitle(QCoreApplication::translate("PatusMainWindow", "Table", nullptr));
        le_tableName->setText(QString());
        le_tableName->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Name", nullptr));
        le_tableId->setText(QString());
        le_tableId->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Table Number", nullptr));
        le_tableSeats->setText(QString());
        le_tableSeats->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Number of seats", nullptr));
        le_tableComment->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Comment", nullptr));
        btn_tableAdd->setText(QString());
        btn_tableEdit->setText(QString());
        btn_tableDelete->setText(QString());
        btn_tableClear->setText(QString());
        tw_database->setTabText(tw_database->indexOf(tab_table), QString());
        groupBox->setTitle(QCoreApplication::translate("PatusMainWindow", "History", nullptr));
        tw_database->setTabText(tw_database->indexOf(tab_pointer), QString());
        gb_stock->setTitle(QCoreApplication::translate("PatusMainWindow", "Stock", nullptr));
        le_stockProductName->setText(QString());
        le_stockProductName->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Name", nullptr));
        le_stockUnit->setText(QString());
        le_stockUnit->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Stock unit", nullptr));
        le_stockQuantity->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Stock quantity", nullptr));
        cb_stockIsIngredient->setText(QCoreApplication::translate("PatusMainWindow", "Is ingredient ?", nullptr));
        btn_stockAdd->setText(QString());
        btn_stockEdit->setText(QString());
        btn_stockDelete->setText(QString());
        btn_stockClear->setText(QString());
        tw_database->setTabText(tw_database->indexOf(tab_stock), QString());
        gb_doccuments->setTitle(QCoreApplication::translate("PatusMainWindow", "Doccuments", nullptr));
        le_docName->setText(QString());
        le_docName->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Name", nullptr));
        dte_docDate->setDisplayFormat(QCoreApplication::translate("PatusMainWindow", "yyyy-MM-dd HH:mm:ss", nullptr));
        le_docComment->setText(QString());
        le_docComment->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Comment", nullptr));
        le_docPath->setText(QString());
        le_docPath->setPlaceholderText(QCoreApplication::translate("PatusMainWindow", "Doc extension", nullptr));
        btn_docAddFile->setText(QString());
        btn_docOpenFile->setText(QString());
        btn_docClearFile->setText(QString());
        btn_docAdd->setText(QString());
        btn_docEdit->setText(QString());
        btn_docDelete->setText(QString());
        btn_docClear->setText(QString());
        tw_database->setTabText(tw_database->indexOf(tab_uploader), QString());
        gb_tableOwnership->setTitle(QCoreApplication::translate("PatusMainWindow", "Table Ownership", nullptr));
        btn_tableOwnershipAdd->setText(QString());
        btn_tableOwnershipEdit->setText(QString());
        btn_tableOwnershipDelete->setText(QString());
        btn_tableOwnershipClear->setText(QString());
        tw_database->setTabText(tw_database->indexOf(tab_tableOwnership), QString());
        label_30->setText(QCoreApplication::translate("PatusMainWindow", "Mourad", nullptr));
        pushButton_52->setText(QCoreApplication::translate("PatusMainWindow", "Send", nullptr));
        pushButton_53->setText(QCoreApplication::translate("PatusMainWindow", "Ring", nullptr));
        label_42->setText(QCoreApplication::translate("PatusMainWindow", "Mourad", nullptr));
        pushButton_66->setText(QCoreApplication::translate("PatusMainWindow", "Send", nullptr));
        pushButton_67->setText(QCoreApplication::translate("PatusMainWindow", "Ring", nullptr));
        label_43->setText(QCoreApplication::translate("PatusMainWindow", "Mourad", nullptr));
        pushButton_68->setText(QCoreApplication::translate("PatusMainWindow", "Send", nullptr));
        pushButton_69->setText(QCoreApplication::translate("PatusMainWindow", "Ring", nullptr));
        l_version->setText(QCoreApplication::translate("PatusMainWindow", "Patus 1.0.1", nullptr));
        l_serverStatus->setText(QCoreApplication::translate("PatusMainWindow", "Server Starting", nullptr));
        l_creator->setText(QCoreApplication::translate("PatusMainWindow", "Made by Lablack Mourad", nullptr));
        btn_logs->setText(QString());
        btn_notification_clear->setText(QCoreApplication::translate("PatusMainWindow", "Clear all notifications", nullptr));
    } // retranslateUi

};

namespace Ui {
    class PatusMainWindow: public Ui_PatusMainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // PATUSINTERFACE_H
