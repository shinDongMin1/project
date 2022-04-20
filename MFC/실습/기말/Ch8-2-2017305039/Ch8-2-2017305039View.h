
// Ch8-2-2017305039View.h: CCh822017305039View 클래스의 인터페이스
//

#pragma once


class CCh822017305039View : public CView
{
protected: // serialization에서만 만들어집니다.
	CCh822017305039View() noexcept;
	DECLARE_DYNCREATE(CCh822017305039View)

// 특성입니다.
public:
	CCh822017305039Doc* GetDocument() const;

// 작업입니다.
public:
	int m_ptx;
	int m_pty;
// 재정의입니다.
public:
	virtual void OnDraw(CDC* pDC);  // 이 뷰를 그리기 위해 재정의되었습니다.
	virtual BOOL PreCreateWindow(CREATESTRUCT& cs);
protected:
	virtual BOOL OnPreparePrinting(CPrintInfo* pInfo);
	virtual void OnBeginPrinting(CDC* pDC, CPrintInfo* pInfo);
	virtual void OnEndPrinting(CDC* pDC, CPrintInfo* pInfo);

// 구현입니다.
public:
	virtual ~CCh822017305039View();
#ifdef _DEBUG
	virtual void AssertValid() const;
	virtual void Dump(CDumpContext& dc) const;
#endif

protected:

// 생성된 메시지 맵 함수
protected:
	DECLARE_MESSAGE_MAP()
public:
	virtual void OnInitialUpdate();
};

#ifndef _DEBUG  // Ch8-2-2017305039View.cpp의 디버그 버전
inline CCh822017305039Doc* CCh822017305039View::GetDocument() const
   { return reinterpret_cast<CCh822017305039Doc*>(m_pDocument); }
#endif

