
// MFCApplication1Doc.cpp: CMFCApplication1Doc 클래스의 구현
//

#include "pch.h"
#include "framework.h"
// SHARED_HANDLERS는 미리 보기, 축소판 그림 및 검색 필터 처리기를 구현하는 ATL 프로젝트에서 정의할 수 있으며
// 해당 프로젝트와 문서 코드를 공유하도록 해 줍니다.
#ifndef SHARED_HANDLERS
#include "MFCApplication1.h"
#endif

#include "MFCApplication1Doc.h"

#include <propkey.h>

#ifdef _DEBUG
#define new DEBUG_NEW
#endif

#define BLACK RGB(0,0,0)
#define RED RGB(255,0,0)
#define BLUE RGB(51,51,255)
#define YELLOW RGB(255,204,51)
// CMFCApplication1Doc

IMPLEMENT_DYNCREATE(CMFCApplication1Doc, CDocument)

BEGIN_MESSAGE_MAP(CMFCApplication1Doc, CDocument)
	ON_COMMAND(ID_DATAIN, &CMFCApplication1Doc::OnDatain)
//	ON_COMMAND(ID_BLUE, &CMFCApplication1Doc::OnBlue)
//	ON_COMMAND(ID_RED, &CMFCApplication1Doc::OnRed)
//	ON_COMMAND(ID_YELLOW, &CMFCApplication1Doc::OnYellow)
ON_COMMAND(ID_BLUE, &CMFCApplication1Doc::OnBlue)
ON_COMMAND(ID_RED, &CMFCApplication1Doc::OnRed)
END_MESSAGE_MAP()


// CMFCApplication1Doc 생성/소멸

CMFCApplication1Doc::CMFCApplication1Doc() noexcept
{
	// TODO: 여기에 일회성 생성 코드를 추가합니다.

}

CMFCApplication1Doc::~CMFCApplication1Doc()
{
}

BOOL CMFCApplication1Doc::OnNewDocument()
{
	if (!CDocument::OnNewDocument())
		return FALSE;

	// TODO: 여기에 재초기화 코드를 추가합니다.
	// SDI 문서는 이 문서를 다시 사용합니다.

	return TRUE;
}




// CMFCApplication1Doc serialization

void CMFCApplication1Doc::Serialize(CArchive& ar)
{
	if (ar.IsStoring())
	{
		// TODO: 여기에 저장 코드를 추가합니다.
	}
	else
	{
		// TODO: 여기에 로딩 코드를 추가합니다.
	}
}

#ifdef SHARED_HANDLERS

// 축소판 그림을 지원합니다.
void CMFCApplication1Doc::OnDrawThumbnail(CDC& dc, LPRECT lprcBounds)
{
	// 문서의 데이터를 그리려면 이 코드를 수정하십시오.
	dc.FillSolidRect(lprcBounds, RGB(255, 255, 255));

	CString strText = _T("TODO: implement thumbnail drawing here");
	LOGFONT lf;

	CFont* pDefaultGUIFont = CFont::FromHandle((HFONT) GetStockObject(DEFAULT_GUI_FONT));
	pDefaultGUIFont->GetLogFont(&lf);
	lf.lfHeight = 36;

	CFont fontDraw;
	fontDraw.CreateFontIndirect(&lf);

	CFont* pOldFont = dc.SelectObject(&fontDraw);
	dc.DrawText(strText, lprcBounds, DT_CENTER | DT_WORDBREAK);
	dc.SelectObject(pOldFont);
}

// 검색 처리기를 지원합니다.
void CMFCApplication1Doc::InitializeSearchContent()
{
	CString strSearchContent;
	// 문서의 데이터에서 검색 콘텐츠를 설정합니다.
	// 콘텐츠 부분은 ";"로 구분되어야 합니다.

	// 예: strSearchContent = _T("point;rectangle;circle;ole object;");
	SetSearchContent(strSearchContent);
}

void CMFCApplication1Doc::SetSearchContent(const CString& value)
{
	if (value.IsEmpty())
	{
		RemoveChunk(PKEY_Search_Contents.fmtid, PKEY_Search_Contents.pid);
	}
	else
	{
		CMFCFilterChunkValueImpl *pChunk = nullptr;
		ATLTRY(pChunk = new CMFCFilterChunkValueImpl);
		if (pChunk != nullptr)
		{
			pChunk->SetTextValue(PKEY_Search_Contents, value, CHUNK_TEXT);
			SetChunkValue(pChunk);
		}
	}
}

#endif // SHARED_HANDLERS

// CMFCApplication1Doc 진단

#ifdef _DEBUG
void CMFCApplication1Doc::AssertValid() const
{
	CDocument::AssertValid();
}

void CMFCApplication1Doc::Dump(CDumpContext& dc) const
{
	CDocument::Dump(dc);
}
#endif //_DEBUG


// CMFCApplication1Doc 명령


CString CMFCApplication1Doc::GetText()
{
	// TODO: 여기에 구현 코드 추가.
	return m_strData;
}


void CMFCApplication1Doc::SetText(CString strin)
{
	m_strData = strin;
	UpdateAllViews(NULL);
	// TODO: 여기에 구현 코드 추가.
}


void CMFCApplication1Doc::OnDatain()
{
	CTextDlg m_Dlg;

	m_Dlg.m_strtextin = GetText();
	if (m_Dlg.DoModal() == IDOK)
		SetText(m_Dlg.m_strtextin);
	// TODO: 여기에 명령 처리기 코드를 추가합니다.
}


void CMFCApplication1Doc::ColorSet(COLORREF color)
{
	// TODO: 여기에 구현 코드 추가.
	m_curColor = color;
	UpdateAllViews(NULL);
}


COLORREF CMFCApplication1Doc::colorGet()
{
	// TODO: 여기에 구현 코드 추가.
	return m_curColor;
}


//void CMFCApplication1Doc::OnBlue()
//{
//	// TODO: 여기에 명령 처리기 코드를 추가합니다.
//	ColorSet(BLUE);
//}


//void CMFCApplication1Doc::OnRed()
//{
//	// TODO: 여기에 명령 처리기 코드를 추가합니다.
//	ColorSet(RED);
//}


//void CMFCApplication1Doc::OnYellow()
//{
//	// TODO: 여기에 명령 처리기 코드를 추가합니다.
//	ColorSet(YELLOW);
//}


void CMFCApplication1Doc::OnBlue()
{
	// TODO: 여기에 명령 처리기 코드를 추가합니다.
	ColorSet(BLUE);
}


void CMFCApplication1Doc::OnRed()
{
	// TODO: 여기에 명령 처리기 코드를 추가합니다.
	ColorSet(RED);
}
