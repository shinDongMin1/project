
// Ch8-2-2017305039View.cpp: CCh822017305039View 클래스의 구현
//

#include "pch.h"
#include "framework.h"
// SHARED_HANDLERS는 미리 보기, 축소판 그림 및 검색 필터 처리기를 구현하는 ATL 프로젝트에서 정의할 수 있으며
// 해당 프로젝트와 문서 코드를 공유하도록 해 줍니다.
#ifndef SHARED_HANDLERS
#include "Ch8-2-2017305039.h"
#endif

#include "Ch8-2-2017305039Doc.h"
#include "Ch8-2-2017305039View.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// CCh822017305039View

IMPLEMENT_DYNCREATE(CCh822017305039View, CView)

BEGIN_MESSAGE_MAP(CCh822017305039View, CView)
	// 표준 인쇄 명령입니다.
	ON_COMMAND(ID_FILE_PRINT, &CView::OnFilePrint)
	ON_COMMAND(ID_FILE_PRINT_DIRECT, &CView::OnFilePrint)
	ON_COMMAND(ID_FILE_PRINT_PREVIEW, &CView::OnFilePrintPreview)
END_MESSAGE_MAP()

// CCh822017305039View 생성/소멸

CCh822017305039View::CCh822017305039View() noexcept
{
	// TODO: 여기에 생성 코드를 추가합니다.

}

CCh822017305039View::~CCh822017305039View()
{
}

BOOL CCh822017305039View::PreCreateWindow(CREATESTRUCT& cs)
{
	// TODO: CREATESTRUCT cs를 수정하여 여기에서
	//  Window 클래스 또는 스타일을 수정합니다.

	return CView::PreCreateWindow(cs);
}

// CCh822017305039View 그리기

void CCh822017305039View::OnDraw(CDC* pDC)
{
	CCh822017305039Doc* pDoc = GetDocument();
	ASSERT_VALID(pDoc);
	if (!pDoc)
		return;

	// TODO: 여기에 원시 데이터에 대한 그리기 코드를 추가합니다.
	RECT rect;
	rect.left = m_ptx - 30;
	rect.top = m_pty - 30;
	rect.right = m_ptx + 50;
	rect.bottom = m_pty + 50;
	
	pDC->SelectStockObject(GRAY_BRUSH);
	pDC->Rectangle(&rect);
	pDC->SelectStockObject(BLACK_BRUSH);
	pDC->Ellipse(200, 200, 300, 300);
	pDC->TextOutW(20, 20, _T("2017305039신동민 사각형/타원 그리기 다중 문서 예제"));

}


// CCh822017305039View 인쇄

BOOL CCh822017305039View::OnPreparePrinting(CPrintInfo* pInfo)
{
	// 기본적인 준비
	return DoPreparePrinting(pInfo);
}

void CCh822017305039View::OnBeginPrinting(CDC* /*pDC*/, CPrintInfo* /*pInfo*/)
{
	// TODO: 인쇄하기 전에 추가 초기화 작업을 추가합니다.
}

void CCh822017305039View::OnEndPrinting(CDC* /*pDC*/, CPrintInfo* /*pInfo*/)
{
	// TODO: 인쇄 후 정리 작업을 추가합니다.
}


// CCh822017305039View 진단

#ifdef _DEBUG
void CCh822017305039View::AssertValid() const
{
	CView::AssertValid();
}

void CCh822017305039View::Dump(CDumpContext& dc) const
{
	CView::Dump(dc);
}

CCh822017305039Doc* CCh822017305039View::GetDocument() const // 디버그되지 않은 버전은 인라인으로 지정됩니다.
{
	ASSERT(m_pDocument->IsKindOf(RUNTIME_CLASS(CCh822017305039Doc)));
	return (CCh822017305039Doc*)m_pDocument;
}
#endif //_DEBUG


// CCh822017305039View 메시지 처리기


void CCh822017305039View::OnInitialUpdate()
{
	CView::OnInitialUpdate();
	CCh822017305039Doc* pDoc = GetDocument();
	// TODO: 여기에 특수화된 코드를 추가 및/또는 기본 클래스를 호출합니다.
	m_ptx = pDoc->m_ptx;
	m_pty = pDoc->m_pty;
}
