
// MFCApplication1View.cpp: CMFCApplication1View 클래스의 구현
//

#include "pch.h"
#include "framework.h"
// SHARED_HANDLERS는 미리 보기, 축소판 그림 및 검색 필터 처리기를 구현하는 ATL 프로젝트에서 정의할 수 있으며
// 해당 프로젝트와 문서 코드를 공유하도록 해 줍니다.
#ifndef SHARED_HANDLERS
#include "MFCApplication1.h"
#endif

#include "MFCApplication1Doc.h"
#include "MFCApplication1View.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// CMFCApplication1View

IMPLEMENT_DYNCREATE(CMFCApplication1View, CView)

BEGIN_MESSAGE_MAP(CMFCApplication1View, CView)
	// 표준 인쇄 명령입니다.
	ON_COMMAND(ID_FILE_PRINT, &CView::OnFilePrint)
	ON_COMMAND(ID_FILE_PRINT_DIRECT, &CView::OnFilePrint)
	ON_COMMAND(ID_FILE_PRINT_PREVIEW, &CView::OnFilePrintPreview)
	ON_COMMAND(ID_CIR, &CMFCApplication1View::OnCir)
	ON_COMMAND(ID_RECT, &CMFCApplication1View::OnRect)
	ON_COMMAND(ID_LINE, &CMFCApplication1View::OnLine)
	ON_COMMAND(ID_CROSS, &CMFCApplication1View::OnCross)
	ON_COMMAND(ID_APPLE, &CMFCApplication1View::OnApple)
	ON_COMMAND(ID_STAR, &CMFCApplication1View::OnStar)
END_MESSAGE_MAP()

// CMFCApplication1View 생성/소멸

CMFCApplication1View::CMFCApplication1View() noexcept
{
	// TODO: 여기에 생성 코드를 추가합니다.

}

CMFCApplication1View::~CMFCApplication1View()
{
}

BOOL CMFCApplication1View::PreCreateWindow(CREATESTRUCT& cs)
{
	// TODO: CREATESTRUCT cs를 수정하여 여기에서
	//  Window 클래스 또는 스타일을 수정합니다.

	return CView::PreCreateWindow(cs);
}

// CMFCApplication1View 그리기

void CMFCApplication1View::OnDraw(CDC* pDC)
{
	CMFCApplication1Doc* pDoc = GetDocument();
	ASSERT_VALID(pDoc);
	if (!pDoc)
		return;
	// TODO: 여기에 원시 데이터에 대한 그리기 코드를 추가합니다.
	CFont font, * pold;

	font.CreatePointFont(300, _T("Broadway"));
	pold = (CFont*)pDC->SelectObject(&font);
	CString srtin1 = _T(" << 2017305039 신동민 >>");
	CString srtin2 = pDoc->GetText();
	pDC->SetTextColor(RGB(0, 0, 0));
	pDC->TextOutW(0, 20, srtin1);

	pDC->SetBkColor(RGB(255, 255, 255));
	pDC->SetTextColor(pDoc->colorGet());

	pDC->TextOutW(50, 100, srtin2);

	switch (m_nOption) {
	case 1: {
		CBrush brush(RGB(0, 255, 0));
		CBrush* poldBrush = pDC->SelectObject(&brush);
		pDC->Ellipse(200, 200, 400, 400);
		brush.DeleteObject();
		break;
	}
	case 2: {
		CBrush brush(RGB(150, 0, 150));
		CBrush* poldBrush = pDC->SelectObject(&brush);
		pDC->Rectangle(200, 200, 400, 400);
		brush.DeleteObject();
		break;
	}
	case 3: {
		CDC* pDC = GetDC();
		int nPentype[] = { PS_SOLID, PS_DOT, PS_DASHDOT, PS_DASH, PS_DASHDOTDOT };

		for (int i = 0; i < sizeof(nPentype) / sizeof(nPentype[0]); i++) {
			CPen pen(nPentype[i], 1, RGB(0, 0, 255));
			pDC->SelectObject(&pen);

			pDC->MoveTo(100, 200 + i * 50);
			pDC->LineTo(500, 200 + i * 50);

			pDC->MoveTo(100, 200 + i * 50);
			pDC->LineTo(500, 300 + i * 50);
		}
		break;
	}
	case 4: {
		CBrush brush(HS_DIAGCROSS, RGB(255, 90, 0));
		CBrush* poldBrush = pDC->SelectObject(&brush);
		pDC->RoundRect(200, 200, 400, 400, 50, 50);
		pDC->SelectObject(poldBrush);
		brush.DeleteObject();
		break;
	}
	case 5: {
		CBitmap bitmap;
		bitmap.LoadBitmap(IDB_BITMAP1);
		CBrush brush(&bitmap);

		CBrush* poldBrush = pDC->SelectObject(&brush);
		pDC->SetBkColor(TRANSPARENT);
		pDC->RoundRect(200, 200, 400, 400, 50, 50);
		pDC->SelectObject(poldBrush);
		brush.DeleteObject();
		break;
	}
	case 6: {
		CBitmap bitmap;
		bitmap.LoadBitmap(IDB_BITMAP2);
		CBrush brush(&bitmap);

		CBrush* poldBrush = pDC->SelectObject(&brush);
		pDC->SetBkColor(TRANSPARENT);
		pDC->RoundRect(200, 200, 400, 400, 50, 50);
		pDC->SelectObject(poldBrush);
		brush.DeleteObject();
		break;
	}
	}
}


// CMFCApplication1View 인쇄

BOOL CMFCApplication1View::OnPreparePrinting(CPrintInfo* pInfo)
{
	// 기본적인 준비
	return DoPreparePrinting(pInfo);
}

void CMFCApplication1View::OnBeginPrinting(CDC* /*pDC*/, CPrintInfo* /*pInfo*/)
{
	// TODO: 인쇄하기 전에 추가 초기화 작업을 추가합니다.
}

void CMFCApplication1View::OnEndPrinting(CDC* /*pDC*/, CPrintInfo* /*pInfo*/)
{
	// TODO: 인쇄 후 정리 작업을 추가합니다.
}


// CMFCApplication1View 진단

#ifdef _DEBUG
void CMFCApplication1View::AssertValid() const
{
	CView::AssertValid();
}

void CMFCApplication1View::Dump(CDumpContext& dc) const
{
	CView::Dump(dc);
}

CMFCApplication1Doc* CMFCApplication1View::GetDocument() const // 디버그되지 않은 버전은 인라인으로 지정됩니다.
{
	ASSERT(m_pDocument->IsKindOf(RUNTIME_CLASS(CMFCApplication1Doc)));
	return (CMFCApplication1Doc*)m_pDocument;
}
#endif //_DEBUG


// CMFCApplication1View 메시지 처리기


void CMFCApplication1View::OnCir()
{
	// TODO: 여기에 명령 처리기 코드를 추가합니다.
	m_nOption = 1;
	Invalidate();
}


void CMFCApplication1View::OnRect()
{
	// TODO: 여기에 명령 처리기 코드를 추가합니다.
	m_nOption = 2;
	Invalidate();
}


void CMFCApplication1View::OnLine()
{
	// TODO: 여기에 명령 처리기 코드를 추가합니다.
	m_nOption = 3;
	Invalidate();
}


void CMFCApplication1View::OnCross()
{
	// TODO: 여기에 명령 처리기 코드를 추가합니다.
	m_nOption = 4;
	Invalidate();
}


void CMFCApplication1View::OnApple()
{
	// TODO: 여기에 명령 처리기 코드를 추가합니다.
	m_nOption = 5;
	Invalidate();
}


void CMFCApplication1View::OnStar()
{
	// TODO: 여기에 명령 처리기 코드를 추가합니다.
	m_nOption = 6;
	Invalidate();
}
