// CTextDlg.cpp: 구현 파일
//

#include "pch.h"
#include "MFCApplication1.h"
#include "CTextDlg.h"
#include "afxdialogex.h"


// CTextDlg 대화 상자

IMPLEMENT_DYNAMIC(CTextDlg, CDialogEx)

CTextDlg::CTextDlg(CWnd* pParent /*=nullptr*/)
	: CDialogEx(IDD_DIALOG1, pParent)
	, m_strtextin(_T(""))
{

}

CTextDlg::~CTextDlg()
{
}

void CTextDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialogEx::DoDataExchange(pDX);
	DDX_Text(pDX, IDC_EDIT1, m_strtextin);
}


BEGIN_MESSAGE_MAP(CTextDlg, CDialogEx)
//	ON_COMMAND(ID_DATAIN, &CTextDlg::OnDatain)
END_MESSAGE_MAP()


// CTextDlg 메시지 처리기

