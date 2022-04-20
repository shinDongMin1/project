
// ChildView.cpp: CChildView 클래스의 구현
//

#include "pch.h"
#include "framework.h"
#include "CH7-1-305039.h"
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
	
	// TODO: 여기에 메시지 처리기 코드를 추가합니다.
	CRect rect;
	GetClientRect(&rect);

	dc.SetTextColor(RGB(255,0,0));
	dc.SetBkColor(RGB(255, 255, 0));
	dc.DrawText(CString("Dream Come TRUE!"), &rect, 0);
	dc.DrawText(CString("꿈은 이루어진다."), &rect, DT_CENTER | DT_VCENTER| DT_SINGLELINE);

	dc.SetTextAlign(TA_CENTER); //한번 정하면 가운데로감
	dc.SetTextColor(RGB(0, 0, 255));
	dc.SetBkColor(RGB(0, 255, 0));
	dc.TextOutW(rect.right/2 , 3*rect.bottom/4,CString("뜻이 있는 곳에 길이 있다."));
	// 그리기 메시지에 대해서는 CWnd::OnPaint()를 호출하지 마십시오.
	//dc.SetTextAlign(TA_RIGHT);
	dc.SetTextColor(RGB(0, 0, 0));
	dc.SetBkColor(RGB(200, 200, 200));
	dc.TextOutW(rect.right / 2, 1 * rect.bottom / 4, CString("2017305039 신동민"));
}

