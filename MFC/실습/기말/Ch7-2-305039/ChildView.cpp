
// ChildView.cpp: CChildView 클래스의 구현
//

#include "pch.h"
#include "framework.h"
#include "Ch7-2-305039.h"
#include "ChildView.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// CChildView

CChildView::CChildView()
{
}

CChildView::~CChildView()
{
}


BEGIN_MESSAGE_MAP(CChildView, CWnd)
	ON_WM_PAINT()
END_MESSAGE_MAP()



// CChildView 메시지 처리기

BOOL CChildView::PreCreateWindow(CREATESTRUCT& cs) 
{
	if (!CWnd::PreCreateWindow(cs))
		return FALSE;

	cs.dwExStyle |= WS_EX_CLIENTEDGE;
	cs.style &= ~WS_BORDER;
	cs.lpszClass = AfxRegisterWndClass(CS_HREDRAW|CS_VREDRAW|CS_DBLCLKS, 
		::LoadCursor(nullptr, IDC_ARROW), reinterpret_cast<HBRUSH>(COLOR_WINDOW+1), nullptr);

	return TRUE;
}

void CChildView::OnPaint() 
{
	CPaintDC dc(this); // 그리기를 위한 디바이스 컨텍스트입니다.
	CRect rect;
	GetClientRect(&rect);
	// TODO: 여기에 메시지 처리기 코드를 추가합니다.
	CPen pen(PS_SOLID, 1, RGB(0, 0, 0));

	dc.SelectObject(&pen);
	dc.Rectangle(100, 100, 200, 200);
	CPen pen1(PS_SOLID, 20, RGB(0, 255, 0));
	dc.SelectObject(&pen1);
	dc.Ellipse(100, 100, 200, 200);

	dc.SelectObject(&pen);
	dc.Rectangle(300, 100, 400, 200);
	CPen pen2(PS_INSIDEFRAME, 20, RGB(0, 255, 0));
	dc.SelectObject(&pen2);
	dc.Ellipse(300, 100, 400, 200);


	dc.SetTextColor(RGB(0, 0, 0));
	dc.DrawText(CString("2017305039신동민"), &rect, DT_CENTER | DT_VCENTER | DT_SINGLELINE);
	CPen pen3(PS_SOLID, 1, RGB(255, 90, 255));
	dc.SelectObject(&pen3);
	dc.Rectangle(500, 400, 900, 600);
	// 그리기 메시지에 대해서는 CWnd::OnPaint()를 호출하지 마십시오.
}

