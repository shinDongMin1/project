
// Ch9-2017305039Dlg.cpp: 구현 파일
//

#include "pch.h"
#include "framework.h"
#include "Ch9-2017305039.h"
#include "Ch9-2017305039Dlg.h"
#include "afxdialogex.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// 응용 프로그램 정보에 사용되는 CAboutDlg 대화 상자입니다.

class CAboutDlg : public CDialogEx
{
public:
	CAboutDlg();

// 대화 상자 데이터입니다.
#ifdef AFX_DESIGN_TIME
	enum { IDD = IDD_ABOUTBOX };
#endif

	protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV 지원입니다.

// 구현입니다.
protected:
	DECLARE_MESSAGE_MAP()
};

CAboutDlg::CAboutDlg() : CDialogEx(IDD_ABOUTBOX)
{
}

void CAboutDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialogEx::DoDataExchange(pDX);
}

BEGIN_MESSAGE_MAP(CAboutDlg, CDialogEx)
END_MESSAGE_MAP()


// CCh92017305039Dlg 대화 상자



CCh92017305039Dlg::CCh92017305039Dlg(CWnd* pParent /*=nullptr*/)
	: CDialogEx(IDD_CH92017305039_DIALOG, pParent)
{
	m_hIcon = AfxGetApp()->LoadIcon(IDR_MAINFRAME);
}

void CCh92017305039Dlg::DoDataExchange(CDataExchange* pDX)
{
	CDialogEx::DoDataExchange(pDX);
}

BEGIN_MESSAGE_MAP(CCh92017305039Dlg, CDialogEx)
	ON_WM_SYSCOMMAND()
	ON_WM_PAINT()
	ON_WM_QUERYDRAGICON()
	ON_COMMAND(ID_ZOOM_ZOOMIN, &CCh92017305039Dlg::OnZoomZoomin)
	ON_COMMAND(ID_ZOOM_ZOOMOUT, &CCh92017305039Dlg::OnZoomZoomout)
	ON_COMMAND(ID_HELP_ABOUT, &CCh92017305039Dlg::OnHelpAbout)
	ON_COMMAND(ID_FILE_EXIT, &CCh92017305039Dlg::OnFileExit)
	ON_COMMAND(ID_PICTURE_SPORTS, &CCh92017305039Dlg::OnPictureSports)
	ON_COMMAND(ID_PICTURE_WHALE, &CCh92017305039Dlg::OnPictureWhale)
	ON_WM_SIZE()
	ON_BN_CLICKED(IDC_BUTTON1, &CCh92017305039Dlg::OnBnClickedButton1)
END_MESSAGE_MAP()


// CCh92017305039Dlg 메시지 처리기

BOOL CCh92017305039Dlg::OnInitDialog()
{
	CDialogEx::OnInitDialog();

	// 시스템 메뉴에 "정보..." 메뉴 항목을 추가합니다.

	// IDM_ABOUTBOX는 시스템 명령 범위에 있어야 합니다.
	ASSERT((IDM_ABOUTBOX & 0xFFF0) == IDM_ABOUTBOX);
	ASSERT(IDM_ABOUTBOX < 0xF000);

	CMenu* pSysMenu = GetSystemMenu(FALSE);
	if (pSysMenu != nullptr)
	{
		BOOL bNameValid;
		CString strAboutMenu;
		bNameValid = strAboutMenu.LoadString(IDS_ABOUTBOX);
		ASSERT(bNameValid);
		if (!strAboutMenu.IsEmpty())
		{
			pSysMenu->AppendMenu(MF_SEPARATOR);
			pSysMenu->AppendMenu(MF_STRING, IDM_ABOUTBOX, strAboutMenu);
		}
	}

	// 이 대화 상자의 아이콘을 설정합니다.  응용 프로그램의 주 창이 대화 상자가 아닐 경우에는
	//  프레임워크가 이 작업을 자동으로 수행합니다.
	SetIcon(m_hIcon, TRUE);			// 큰 아이콘을 설정합니다.
	SetIcon(m_hIcon, FALSE);		// 작은 아이콘을 설정합니다.

	// TODO: 여기에 추가 초기화 작업을 추가합니다.

	return TRUE;  // 포커스를 컨트롤에 설정하지 않으면 TRUE를 반환합니다.
}

void CCh92017305039Dlg::OnSysCommand(UINT nID, LPARAM lParam)
{
	if ((nID & 0xFFF0) == IDM_ABOUTBOX)
	{
		CAboutDlg dlgAbout;
		dlgAbout.DoModal();
	}
	else
	{
		CDialogEx::OnSysCommand(nID, lParam);
	}
}

// 대화 상자에 최소화 단추를 추가할 경우 아이콘을 그리려면
//  아래 코드가 필요합니다.  문서/뷰 모델을 사용하는 MFC 애플리케이션의 경우에는
//  프레임워크에서 이 작업을 자동으로 수행합니다.

void CCh92017305039Dlg::OnPaint()
{
	if (IsIconic())
	{
		CPaintDC dc(this); // 그리기를 위한 디바이스 컨텍스트입니다.

		SendMessage(WM_ICONERASEBKGND, reinterpret_cast<WPARAM>(dc.GetSafeHdc()), 0);

		// 클라이언트 사각형에서 아이콘을 가운데에 맞춥니다.
		int cxIcon = GetSystemMetrics(SM_CXICON);
		int cyIcon = GetSystemMetrics(SM_CYICON);
		CRect rect;
		GetClientRect(&rect);
		int x = (rect.Width() - cxIcon + 1) / 2;
		int y = (rect.Height() - cyIcon + 1) / 2;

		// 아이콘을 그립니다.
		dc.DrawIcon(x, y, m_hIcon);
	}
	else
	{
		CPaintDC dc(this);
		HBITMAP hBitmap;
		HDC hMemDC = ::CreateCompatibleDC(NULL);

		if (m_menu == ID_PICTURE_SPORTS)
			hBitmap = ::LoadBitmap(m_hInstance, MAKEINTRESOURCE(IDB_BITMAP1));
		else if (m_menu == ID_PICTURE_WHALE)
			hBitmap = ::LoadBitmap(m_hInstance, MAKEINTRESOURCE(IDB_BITMAP2));
		else
			hBitmap = NULL;

		SelectObject(hMemDC, hBitmap);

		switch (m_menuID) {
		case ID_ZOOM_ZOOMIN: {
			if(m_menu == ID_PICTURE_SPORTS)		/* 사진이 전체화면에 보여진다. */
				::StretchBlt(dc.m_hDC, 0, 0, m_nWidth, m_nHeight, hMemDC, 0, 0, 300, 300, SRCCOPY);
			else
				::StretchBlt(dc.m_hDC, 0, 0, m_nWidth, m_nHeight, hMemDC, 0, 0, 600, 464, SRCCOPY);
			break;
		}
		case ID_ZOOM_ZOOMOUT: {
			/* 그림축소- (150,150) 좌표에서 시작, 300×300 사이즈 그림이 그려진다. */
			::StretchBlt(dc.m_hDC, 0, 0, 150, 150, hMemDC, 0, 0, 600, 464, SRCCOPY);
			break;
		}
		default: {
			/* (50,50)좌표에서 시작, 250×250 사이즈 그림이 그려진다. */
			::StretchBlt(dc.m_hDC, 50, 50, 300, 300, hMemDC, 0, 0, 600, 464, SRCCOPY);
		}
		}
		::DeleteDC(hMemDC);
		::DeleteObject(hBitmap);
		CDialogEx::OnPaint();
	}
}

// 사용자가 최소화된 창을 끄는 동안에 커서가 표시되도록 시스템에서
//  이 함수를 호출합니다.
HCURSOR CCh92017305039Dlg::OnQueryDragIcon()
{
	return static_cast<HCURSOR>(m_hIcon);
}



void CCh92017305039Dlg::OnZoomZoomin()
{
	// TODO: 여기에 명령 처리기 코드를 추가합니다.
	m_menuID = ID_ZOOM_ZOOMIN;
	Invalidate();
}


void CCh92017305039Dlg::OnZoomZoomout()
{
	// TODO: 여기에 명령 처리기 코드를 추가합니다.
	m_menuID = ID_ZOOM_ZOOMOUT;
	Invalidate();
}


void CCh92017305039Dlg::OnHelpAbout()
{
	// TODO: 여기에 명령 처리기 코드를 추가합니다.
	CAboutDlg dlg;
	dlg.DoModal();
}


void CCh92017305039Dlg::OnFileExit()
{
	// TODO: 여기에 명령 처리기 코드를 추가합니다.
	OnOK();
}


void CCh92017305039Dlg::OnPictureSports()
{
	// TODO: 여기에 명령 처리기 코드를 추가합니다.
	m_menu = ID_PICTURE_SPORTS;
	Invalidate();
}


void CCh92017305039Dlg::OnPictureWhale()
{
	// TODO: 여기에 명령 처리기 코드를 추가합니다.
	m_menu = ID_PICTURE_WHALE;
	Invalidate();
}


void CCh92017305039Dlg::OnSize(UINT nType, int cx, int cy)
{
	CDialogEx::OnSize(nType, cx, cy);

	// TODO: 여기에 메시지 처리기 코드를 추가합니다.
	m_nWidth = cx;
	m_nHeight = cy;
	Invalidate();
}


void CCh92017305039Dlg::OnBnClickedButton1()
{
	// TODO: 여기에 컨트롤 알림 처리기 코드를 추가합니다.
	OnOK();
}
