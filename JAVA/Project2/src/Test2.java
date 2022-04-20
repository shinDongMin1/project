import java.io.*;
import java.util.Scanner;


class Fraction{
	int numerator;
	int denominator;
	int gcd(int x, int y) {return (y!=0)? gcd(y, x%y):x;} //최대공약수 
	Fraction reduce(Fraction f) {int divisor; divisor = gcd(f.numerator, f.denominator); //기약분수
								 f.numerator /= divisor; f.denominator /= divisor; 	
								 return f;}
	Fraction(int num, int denom) {numerator = num; denominator = denom;}
	
	public Fraction add(Fraction f) {numerator = numerator*f.denominator+f.numerator*denominator;
									 denominator = denominator*f.denominator;
									 return reduce(this);}
	public Fraction sub(Fraction f) {numerator = numerator*f.denominator-f.numerator*denominator;
	 								 denominator = denominator*f.denominator;
	 								 return reduce(this);}
	public Fraction mul(Fraction f) {numerator = numerator*f.numerator;
	 								 denominator = denominator*f.denominator;
	 								 return reduce(this);}
	public Fraction div(Fraction f) {numerator = numerator*f.denominator;
	 								 denominator = denominator*f.numerator;
	 								 return reduce(this);}
	public String toString() {String s = numerator+"/"+denominator; return s;}
	
}
class Complex{
	double real;
	double image;
	Complex() {real = 0; image = 0;}
	Complex(double num) {real = num; image = num;}
	Complex(double num1, double num2) {real = num1; image = num2;}
	
	public Complex addComplex(Complex f) {real = real+f.real; image = image+f.image; return this;}
	public Complex subComplex(Complex f) {real = real-f.real; image = image-f.image; return this;}
	public Complex mulComplex(Complex f) {real = (real*f.real)-(image*f.image);
										  image = (real*f.image)+(f.real*image); return this;}
	public Complex divComplex(Complex f) {real = (real*f.real)+(image*f.image) / ((f.real*f.real)+(f.image*f.image));
	  									  image = (f.real*image)-(real*f.image) / ((f.real*f.real)+(f.image*f.image)); 
	  									  return this;}
	public String toString() {
		String s;
	if(real != 0 && image != 0) {
		if(image > 0) {
			if(image == 1)
				s = real+"+i";
			else
				s = real+"+"+image+"i";
		}
		else {
			if(image == -1)
				s = real+"-i";
			else
				s = real+""+image+"i";
		}
	}
	else if(real == 0 && image != 0) {
		if(image == -1)
			s = "-i";
		else if(image == 1)
			s = "i";
		else
			s = image+"i";
	}
	else if(real != 0 && image == 0) {
		s = real+"";
	}
	else
		s = "";
		
	return s;
	}
}


class Outer{
	static class Inter{
		static String str = "???";
		
		Inter(){}
		Inter(String s){str = s;}
		static void print(String s) {
			str = s;
			System.out.println(s);
		}
		static void Sprint() {
			print(str);
		}
	}
}

class SuperClass {
	int val;
	static int supNum = 100;
	SuperClass(){val = 0;}
	SuperClass(int i){val = i;}
	void Output() {System.out.println(val);}
	static String greeting() {return "GOOD";}
	String name() {return "Oak";}
}
class SubClass extends SuperClass {
	int val;
	static int supNum = 200;
	SubClass(int i){super(i);val = i;}
	void Output() {System.out.println(val+","+super.val);}
	static String greeting() {return "Hell";}
	String name() {return "JAVA";}
}

class BaseClass{
	public boolean equals(Object obj) {
		if(getClass() == obj.getClass()) return true;
		else return false;
	}
}
class DerivedClass extends BaseClass{}
class Stack{
	private int[] stack;
	int sp = 0;
	
	Stack(){ stack = new int[100];}
	Stack(int size){ stack = new int[size];}
	//public void push(int data) {stack[sp++] =data;}
	//public int pop() {return stack[--sp];}
	//public void print(int x) {for(int i = 0; i < x; i++) System.out.printf("%-4d ", stack[i]); System.out.println("");}	
	public void push(int data) {if(sp < stack.length) {stack[sp++] = data;} else System.out.print("overflow! ");}
    public int pop() {if(--sp < 0) {sp = 0; System.out.print("underflow! "); return -1;} else return stack[sp];}
    
	//public void push(int data) {if(sp < stack.length) {stack[sp++] = data;} else stack[sp] = data;}  //예외처리-디폴트: 시스템에서 정의된 예외
    //public int pop() {if(--sp < 0) {sp = 0;return stack[-1];} else return stack[sp];}
	
	//public class EmptyStackException extends RuntimeException{           //예외처리-사용자정의: 사용자가 정의한 예외를 throw로 발생/메소드에 처리문이 없으면 throws
	//	public EmptyStackException() {System.out.println("underflow");}
	//}
	//public class OverflowStackException extends RuntimeException{
	//	public OverflowStackException() {System.out.println("overflow");}
	//}
	//public void push(int data) throws OverflowStackException {if(sp == 10) throw new OverflowStackException(); else stack[sp++] =data;}
	//public int pop() throws EmptyStackException { if(sp == 0) throw new EmptyStackException(); return stack[--sp];}

	//public void push(int data) throws IOException {if(sp == 10) throw new IOException(); else stack[sp++] =data;}
	//public int pop() throws IOException {if(sp == 0) throw new IOException(); return stack[--sp];}

}

class Count{
	public static int scount = 0;
	public int count = 0;
	public static void sIncrement() {scount++;}
	public void increment() {count++;}
}

class Sort{
	void swap(int v[], int i, int j) {
		int temp;
		temp = v[i];
		v[i] = v[j];
		v[j] = temp;
	}
	public void Qsort(int a[], int left, int right) {
		int pe;
		int i, last;
		
		if(left >= right) return;
		pe = (left+right)/2;
		swap(a, left, pe);
		last = left;
		for(i = left+1; i <= right; i++) {
			if(a[i] < a[left])
				swap(a, ++last, i);
		}
		swap(a, left, last);
		Qsort(a, left, last-1);
		Qsort(a, left+1, right);
	}
}



public class Test2 {
	static int method(int x, int y) {
		while(x != y)
			if(x > y) x -= y;
			   else y -= x;
		return x;
	}
	static void print(SuperClass obj) {//SubClass오류
		obj.Output();
	}
	public static void main(String[] args) throws java.io.IOException {
		// TODO Auto-generated method stub
		Complex cm1 = new Complex();
		Complex cm2 = new Complex(1);
		Complex cm3 = new Complex(3, 1);
		
		cm1.addComplex(cm2);
		cm2.mulComplex(cm3);
		System.out.println(cm1.toString());
		System.out.println(cm2.toString());
	}

}


/*		Scanner sc = new Scanner(System.in);
		Stack st = new Stack();
		int a, n=0;
		
		System.out.print("입력하시오:");
		while(true) {
			try {
				a= sc.nextInt();
				if(a == 0)
					break;
				n++;
				st.push(a);
				System.out.printf("%-4d ", a);
			}catch(Exception e) {System.out.print("overflow");break;}
		}
		System.out.println("");
		
		if(n > 10)
			st.print(n-1);
		else
			st.print(n);
		while(n-- > 0) {
			try {
				System.out.printf("%-4d ", st.pop());
			}catch(Exception e) {System.out.println("underflow");break;}
		}
		for(int i = 0; i < n; i++) {
			a= sc.nextInt();
			st.push(a);
		}
		try {
			throw new IOException();
		}catch(IOException e) {System.out.println("오류");}
		sc.close();
	}
*/

/*
public class Test1 {

	int x;
	void start() {};
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		Stack st = new Stack(10);
		int num, count=0;
		
		System.out.print("입력하시오:");
		while(true) {
			try {
				num= sc.nextInt();
				if(num == 0)
					break;  
				count++;
				st.push(num); 	//Exception(); try-catch문은 한개만 코드의 분산
			}catch(Exception e) {System.out.println("overflow");break;}
		}
		
		while(count > 0) { 
			try {
				count--;
				System.out.print(st.pop()+" ");
			}catch(IndexOutOfBoundsException e) {System.out.print("underflow");break;}
		}
		System.out.println();
		
		Count c = new Count();
		c.increment(); Count.sIncrement(); c.sIncrement();
		System.out.print("Instance Value = "+ c.count);
		System.out.println(", Static Value = "+ Count.scount);
		
		BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
		int i, j;
		int a, b;
		
		System.out.print("Enter first number : ");
		i = Integer.parseInt(input.readLine());
		System.out.print("Enter second number : ");
		j = Integer.parseInt(input.readLine());
		a = method(i, j);
		System.out.println("a = "+ a);
		b = (i/a) * (j/a) * a;
		System.out.println("b = "+ b);
		
		Sort qsort = new Sort();
		int[] vector= new int[100];
		int index = 0;
		int k = 0;
		
		System.out.print("정렬을 입력하시오:");
		while(true) {
			try {
				num= sc.nextInt();
				if(num == 0)
					break;
				vector[index] = num;
				index++;
			}catch(Exception e) {System.out.println("overflow");break;}
		}
		qsort.Qsort(vector, 0, index-1);
		
		for(k = 0; k < index; k++)
			System.out.printf("%-4d ", vector[k]);
		System.out.println("");
		
		System.out.print(SuperClass.supNum+", "+ SubClass.supNum);
		System.out.println(", "+ SubClass.supNum);
		
		BaseClass b1 = new BaseClass();
		BaseClass b2 = new BaseClass();
		DerivedClass d1 = new DerivedClass();
		DerivedClass d2 = new DerivedClass();
		if(b1.equals(d1))	System.out.println("derived equals base.");
		if(d1.equals(b1))	System.out.println("base equals derived.");
		if(b1.equals(b2))	System.out.println("base equals base.");
		if(d1.equals(d2))	System.out.println("derived equals derived.");

		SuperClass s = new SubClass(1);
		SuperClass obj1 = new SuperClass(1);
		SubClass obj2 = new SubClass(1);
		//SubClass asd = new SuperClass(); 오류
		System.out.println(s.greeting()+", "+s.name());
		print(obj1);
		print(obj2);
		
		sc.close();
		Stack st = new Stack();
		st.push(5); st.push(2); st.push(1);
		System.out.print(st.pop()+" ");
		System.out.print(st.pop()+" ");
		System.out.println(st.pop());
		
		Complex cm1 = new Complex(0);
		Complex cm2 = new Complex(1);
		
		cm1.addComplex(cm2);
		System.out.println(cm1.toString());
		
		Sort a = new Sort();
		int[] b = {5, 8, 4, 6, 1};
		a.Qsort(b, 0, 4);
		for(int k: b)
			System.out.print(k+"");
		System.out.println();
		
		String s = "Hellow";
		Outer.Inter oi = new Outer.Inter(); //객체
		Outer.Inter.Sprint();
		oi.print(s);
		
		System.out.println(SuperClass.supNum+","+SubClass.supNum);
		SuperClass sup = new SuperClass(1);
		SubClass sub = new SubClass(1);
		SuperClass asd = new SubClass(1);
		//SubClass asd = new SuperClass(); 오류
		sup.supNum = 10; sub.supNum = 20;
		System.out.println(SuperClass.supNum+","+SubClass.supNum);
		SuperClass.supNum = 100; SubClass.supNum = 200;
		System.out.println(SuperClass.supNum+","+SubClass.supNum+","+asd.supNum);
		System.out.println(asd.greeting()+","+asd.name());
		sup.Output();
		sub.Output();
		
		BaseClass b1 = new BaseClass();
		BaseClass b2 = new BaseClass();
		BaseClass b3 = new DerivedClass();
		DerivedClass d1 = new DerivedClass();
		DerivedClass d2 = new DerivedClass();
		//DerivedClass d3 = new BaseClass(); 오류
		if(b1.equals(d1))	System.out.println("1.der = base");
		if(d1.equals(b1))	System.out.println("2.base = der");
		if(b1.equals(b2))	System.out.println("3.base = base");
		if(d1.equals(d2))	System.out.println("4.der = der");
		if(b3.equals(b1))	System.out.println("5.객체base");
		if(b3.equals(d1))	System.out.println("6.객체der");
		
		for(int i=1; i < 1000; i++) {
			int sum = 0;
			for(int j=1; j <i; j++) {
				if(i%j == 0)
					sum += j;
			}
			if(i == sum)
				System.out.print(i+" ");
		}
		String[] str = {"A", "B", "C", "D"};
		for(String s1: str) {
			System.out.println(s1);
		}
		for(int i = 0 ;i < 4; i++) {
			System.out.println(str[i]);
		}
		System.out.println(1/2 + " " + 1/2.0);
		
		Scanner sc = new Scanner(System.in);
        int a1; double a2;
        String c;
        System.out.print("수를 입력");
        a1=sc.nextInt();
        a2=sc.nextDouble();
        c = sc.next();
        //int c=gcd(a,b);
        //int d=lcm(a,b);
        System.out.println(a1);
        System.out.println(a2);
        System.out.println(c);
        sc.close();
	}
}*/



