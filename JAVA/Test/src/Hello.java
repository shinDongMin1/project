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
	public int x, y;        //����
	static int xx = 0;      //����-���� ��������� ������ public�� ��� �ٸ������� ��밡�� ������ ��ü�� ���� ����� ��������, 
	                        //�̰Ϳ� ���� �Լ��� static����
	Test(){ x=1; y=2;};
	public void Swap(int x, int y) { int temp; temp = x; x = y; y = temp; }; //�� �Ű�����
	public static void Swap(Test obj) { int temp; temp = obj.x; obj.x = obj.y; obj.y = temp;}; //���� �Ű�����-��ü ����
	public void PrintTest(int... args) {int SUM = 0;for(int i : args) SUM += i;}; //���� �Ű�����
}

/*
BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
		int a, n;
		
		System.out.print("%1$-5.2d �Է�:");
		a = Integer.parseInt(input.readLine());
		//a = System.in.read()-'0';
		
		System.out.print("- # + ' ' 0 , ( �Է�:");
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
java.io.IOException: �Է¶��̺귯��
// <<, >>> ��ȣ ������� / >> ��ȣ �������
// Ŭ����(C++)-��ünew�����Ҵ�, int=O377, OXff(long=255L) double=0.314E1(float=0.314e01f) string(char), �ʵ�(����) / �޼ҵ�(�ൿ)

// ����ó��(C++)-����ð��� �߻��ϴ� ���� / ���������� ���� / �߸��� ���
// throwable- Error(�ɰ��� ����) / Exception(���α׷��Ӱ� ��ĥ �� �ִ� ����) Ŭ����
// class user extends Exception{ user(string s){super(s);}}
// user x = new user();
// try{ throw x(new user("����"));}catch (user e){System.out.printIn(e.getMessage()); }

// ������(�ڹ�)�̺�Ʈ-��Ƽ�׽�ŷ�� sw�� ���α׷� ������ ���� / ���� �������� �ִ� ����ó�� / public void run(){}
// 1)�ý��ۻ�� extends Thread / new Thread();
// 2)�������̽���� implements Runnable / new Thread(new Runnable());

// ���׸�(c++���ø�)-�ڷ����� �Ű������� ���� �� �ִ� 
// template<class T>
// 1)Ŭ���� class App<Type>
// 2)�Լ� T App<T>(T x, T y)

// �Ӹ� - ���� - ����
// ���ֱ���- x=y;-> 4���� ��ū = ���� ���� / �����ڵ� ����ǥ�� 16bit(c��� �ƽ�Ű�ڵ� ����ǥ�� 8bit) / unsigned x
// 1)Ư������- ������(while int) / ������(+ -) / ������([] , ;)
// 2)�Ϲ�����- ��Ī(���� $) / ���ͷ�(���� ���Ƶ� �ڷ����� �ٸ��� �ٸ� ������� �Ǽ���� ���ڻ��'a''\t' ��Ʈ�����"hi" ���Ż��enum ��ü�������NULL) 
// �ڷ���- ������ �������� �� ���� ����
// 1)�⺻�� stack ���� / �Ǽ� / ���� / ��
// 2)������(�����������) heap �迭 / Ŭ���� / �������̽�

//������ ����: NaN(���Ѵ뿬��), ��������
// [] ()
// ++ -- (����) ! (��) ~ (��Ʈ)
// (casting)
// ����+ ����- * / % + - (���)  
// << >> >>> (��Ʈ)
// > >= < <= == != (����) instanceof(ũ��)
// & ^ | (��Ʈ)
// && || (��)
// ? (����)
// = += -= *= /= %= &= ^= |= >>= <<= (����) 
// ũ�� ��ȯ�� ���� �׷ο층(����� / ����ȭ) / ���̵帵(������ / ����ȭ) boolean x
*/
