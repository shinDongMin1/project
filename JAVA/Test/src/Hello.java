import java.io.*;

public class Hello {
	public static void main(String[] args) throws IOException {

		// TODO Auto-generated method stub
		final double p = 3.14;
		System.out.println(Test.xx + " " + p);
		Test obj = new Test();

		obj.xx = 1;
		System.out.println(obj.xx);
		obj.xx = 2;
		System.out.println(obj.xx);
		System.out.println();
		obj.Swap(obj);
		System.out.println(obj.x + " "+ obj.y);
		Test.Swap(obj);
		System.out.println(obj.x + " "+ obj.y);
	}

}
class Test{
	public int x, y;        //각자
	static int xx = 0;      //공용-먼저 만들어지기 때문에 public이 없어도 다른곳에서 사용가능 하지만 객체에 대한 설계상 옮지않음, 
	                        //이것에 관한 함수도 static선언
	Test(){ x=1; y=2;};
	public void Swap(int x, int y) { int temp; temp = x; x = y; y = temp; }; //값 매개변수
	public static void Swap(Test obj) { int temp; temp = obj.x; obj.x = obj.y; obj.y = temp;}; //참조 매개변수-객체 참조
	public void PrintTest(int... args) {int SUM = 0;for(int i : args) SUM += i;}; //가변 매개변수
}

/*
BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
		int a, n;
		
		System.out.print("%1$-5.2d 입력:");
		a = Integer.parseInt(input.readLine());
		//a = System.in.read()-'0';
		
		System.out.print("- # + ' ' 0 , ( 입력:");
		n = Integer.parseInt(input.readLine());
		
		System.out.printf("%2$d, %1$d\n", a, n);
		
		int i = -1;
		int j = 1;
		
		int neg1 = i >> 1;  
		int neg2 = i >>> 1; 
		int neg3 = j << 1;
		int neg4 = j >>> 1;
		
		System.out.println(neg1);
		System.out.println(neg2);
		System.out.println(neg3);
		System.out.println(neg4);
java.io.IOException: 입력라이브러리
// <<, >>> 부호 상관없음 / >> 부호 상관있음
// 클래스(C++)-객체new동적할당, int=O377, OXff(long=255L) double=0.314E1(float=0.314e01f) string(char), 필드(상태) / 메소드(행동)

// 예외처리(C++)-실행시간에 발생하는 에러 / 비정상적인 종료 / 잘못된 결과
// throwable- Error(심각한 오류) / Exception(프로그래머가 고칠 수 있는 오류) 클래스
// class user extends Exception{ user(string s){super(s);}}
// user x = new user();
// try{ throw x(new user("예외"));}catch (user e){System.out.printIn(e.getMessage()); }

// 스레드(자바)이벤트-멀티테스킹을 sw로 프로그램 내에서 구현 / 단일 진행점이 있는 순차처리 / public void run(){}
// 1)시스템상속 extends Thread / new Thread();
// 2)인터페이스상속 implements Runnable / new Thread(new Runnable());

// 제네릭(c++템플릿)-자료형을 매개변수로 가질 수 있다 
// template<class T>
// 1)클래스 class App<Type>
// 2)함수 T App<T>(T x, T y)

// 머리 - 선언 - 문장
// 어휘구조- x=y;-> 4개의 토큰 = 문장 구조 / 유니코드 문자표현 16bit(c언어 아스키코드 문자표현 8bit) / unsigned x
// 1)특수형태- 지정어(while int) / 연산자(+ -) / 구분자([] , ;)
// 2)일반형태- 명칭(변수 $) / 리터럴(값이 같아도 자료형이 다르면 다름 정수상수 실수상수 문자상수'a''\t' 스트링상수"hi" 열거상수enum 객체참조상수NULL) 
// 자료형- 문장을 컴파일할 때 적용 범위
// 1)기본형 stack 정수 / 실수 / 문자 / 논리
// 2)참조형(사용자정의형) heap 배열 / 클래스 / 인터페이스

//연산자 종류: NaN(무한대연산), 좌측결합
// [] ()
// ++ -- (증감) ! (논리) ~ (비트)
// (casting)
// 단항+ 단항- * / % + - (산술)  
// << >> >>> (비트)
// > >= < <= == != (관계) instanceof(크기)
// & ^ | (비트)
// && || (논리)
// ? (조건)
// = += -= *= /= %= &= ^= |= >>= <<= (배정) 
// 크기 변환에 따른 네로우링(명시적 / 협소화) / 와이드링(묵시적 / 광역화) boolean x
*/
