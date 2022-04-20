using System;
using System.Threading;
using System.Drawing;
using System.IO;
using System.Xml.Serialization;          //CTS 라이브러리 자료형
using System.Runtime.Serialization.Formatters;
using System.ComponentModel;
using System.ComponentModel.Design.Serialization;
using Microsoft.VisualBasic.CompilerServices;
using System.Security.Cryptography;
using System.Runtime.InteropServices;

namespace _2017305039신동민
{
    /* class Program{
            static void Main()
            {
                int a=5;
                int b=3;
                int c = Program.Add(a,b);
                Console.WriteLine(c);
                Console.WriteLine("Hello world");
            }

            static int Add(int a, int b)
            {
                return a + b;

            }

        }*/

    /* class Even {
            int evenNumber;
         public Even(int n) {
                evenNumber = (n % 2 == 0) ? n : n + 1;
            }
            public static Even operator++(Even e) {
                e.evenNumber += 2;
                return e;
            }
            public static Even operator--(Even e)
            {
                e.evenNumber -= 2;
                return e;
            }
            public void Printeven() {
                Console.WriteLine("Even Number= " + evenNumber);
            }

        }
        class OperatorApp {
            public static void Main()
            {
                Even e = new Even(4); e.Printeven();
                ++e; e.Printeven();
                --e; e.Printeven();
            }
        }*/

    /*  class CondoperApp {
           public static void Main() {
               int a, b, c, m;
               Console.Write("Enter Numbers : ");
               a = Console.Read()-'0';
               b = Console.Read()-'0';
               c = Console.Read()-'0';
               m = (a > b) ? a : b;
               m = (m > c) ? m : c;
               Console.WriteLine("큰값 : " + m);

           }
       }*/

    /* class CompoundApp {
        public static void Main()
        {
            int n;
            Console.Write("Enter one digit :");
            n = Console.Read() - '0';
            if (n < 0)
                Console.WriteLine("음수");
            else{
                Console.WriteLine(n + " squared is " + (n*n));
                Console.WriteLine(n + " cubed is " + (n * n * n));
            }
        }*/

    /*   class AnotherblockApp {
            public static void Main() {
                int x = 1;
                {
                    int y = 2;
                    Console.WriteLine("block 1: x = " + x + "y = "+ y);
                }
                {
                    int y = 3;
                    Console.WriteLine("block 2: x = " + x + "y = " + y);
                }
            }
        }*/

    /*  class Fraction {
        int num;
        int den;
        public Fraction(int n, int d) {
            num = n;
            den = d;
        }
        public void Point() {
            Console.WriteLine(num + "/" + den);
        }
    }
    class Fract {
        public static void Main() {
            Fraction f = new Fraction(1,2);
            f.Point();
        }
    }*/

    /* class Method {
         void Some() {
             Console.WriteLine("Some1 call");
         }
         void Some(int i)
         {
             Console.WriteLine("Some2 call");
         }
         void Some(int i, int j)
         {
             Console.WriteLine("Some3 call");
         }
         void Some(double i)
         {
             Console.WriteLine("Some4 call");
         }
         static void Main() {
             Method o = new Method();
             o.Some();
             o.Some(526);
             o.Some(45,65);
             o.Some(5.55);
         }
     }*/

    /* class Propertyclass {
         int value;
         public int Value {
             get { return value; }
             set { this.value = value; }
         }
         public void Print() {
             Console.WriteLine("h value = " + value);
         }
     }
     class PropertyApp {
         public static void Main() {
             int n;
             Propertyclass obj = new Propertyclass();
             obj.Value = 100;
             obj.Print();
             n = obj.Value;
             Console.WriteLine("값 : "+n);
         }
     }*/

    /*delegate void Sampledel();
    class Deleclass {
        public void DeleMethod() {
            Console.WriteLine("메소드...");
        }
    }
    class DeleApp {
        public static void Main() {
            Deleclass d = new Deleclass();
            Sampledel S = new Sampledel(d.DeleMethod);
            S();
        }
    }*/
    //제네릭 클래스
    /*class Stack<Type>
    {
        Type[] st = new Type[100];
        int sp = -1;
        public void Push(Type e) {
            st[++sp] = e;   
        }
        public Type Pop() {
            return st[sp--];
        
        }
    }
    class Program { 
    public static void Main (){
            Stack<int> stk1 = new Stack<int>();
            Stack<double> stk2 = new Stack<double>();
            stk1.Push(1); stk1.Push(2); stk1.Push(3);
            stk2.Push(1.5); stk2.Push(2.5); stk2.Push(3.5);
            Console.WriteLine("int : " + stk1.Pop() + ' ' + stk1.Pop() + ' ' + stk1.Pop());
            Console.WriteLine("double : " + stk2.Pop() + ' ' + stk2.Pop() + ' ' + stk2.Pop());
        }
    }*/
    //스레드
    /*class Threadapp {
        static void Threadbody() {
            Console.WriteLine("스레드 몸체");
        }
        public static void Main() {
            ThreadStart ts = new ThreadStart(Threadbody);
            Thread t = new Thread(ts);
            Console.WriteLine("s");
            t.Start();
            Console.WriteLine("e");
        }
    }*/
    //제네릭 함수
    /*class Metapp {
        static void Swap<Type>(ref Type x, ref Type y) {
            Type temp;
            temp = x;
            x = y; y = temp;
        }
        public static void Main() {
            int a = 1, b = 2;double c = 1.5, d = 2.5;
            Console.WriteLine("a = {0}, b = {1}", a, b);
            Swap<int>(ref a, ref b);
            Console.WriteLine("a = {0}, b = {1}", a, b);
            Console.WriteLine("c = {0}, d = {1}", c, d);
            Swap<double>(ref c, ref d);
            Console.WriteLine("c = {0}, d = {1}", c, d);

        }
    }*/
    //스레드
    /*class Threadapp {
        static void Threadbody() {
            for (int i = 0; i < 5; i++) {
                Console.WriteLine(DateTime.Now.Second + " : " + i);
                Thread.Sleep(1000);
            }
        }
        public static void Main() {
            ThreadStart ts = new ThreadStart(Threadbody);
            Thread t = new Thread(ts);
            t.Start();
        }
    }*/
    //기본기
    /* class Program {
        public static void Main() {
            Math.Sqrt(2.0); //루트2 
            Math.Pow(2, 3);  //2^3
            Math.Abs(-10);  //절대값 10
            string s = Console.ReadLine(); //"1 2 3"
            string[] array = s.Split(" "); //{'1','2','3'}
            int a = int.Parse(array[0]);  //'1' -> int a
            int[] iarray = new int[array.Length];
            for (int i = 0; i < array.Length; i++) {
                iarray[i] = int.Parse(array[i]);
            }
            foreach (int i in iarray) {
                Console.Write(i + " ");
            }
        }
    }*/
    //컬러
    /*enum Color { R, G, B, Max = B}
    class Exercisech
    {
        public static void Main()
        {
            Color c = Color.R;
            int i = (int)++c;
            Console.WriteLine("color" + (Color)i);
            c = Color.B;
            Console.WriteLine("color" + (int)c);
            c = Color.Max;
            Console.WriteLine("color" + (int)c);

            int a,b;
            int x = 1;
            int y = 3;
            a = Console.Read() - '0';
            a = Int32.Parse(Console.ReadLine());
            Math.Log(Math.Pow((x - y), 2), Math.Exp(1));
              
        }
    }*/
    //4.12번
    /*
    class Complex {
        public double real;
        public double image;
    
        public Complex() {
            real = 0; image = 0;
        }
        public Complex(double d1) {
            real = d1; image = d1;
        }
        public Complex(double d1, double d2) {
            real = d1; image = d2;
        }
        public void toString() {
            if(image > 1)
                Console.WriteLine("{0}+{1}i", real, image);
            else if(image == 1)
                Console.WriteLine("{0}+i", real);
            else if(image == 0)
                Console.WriteLine("{0}", real);
            else if (image == -1)
                Console.WriteLine("{0}-i", real);
            else
                Console.WriteLine("{0}{1}i", real, image);
        }
        public Complex AddComplex (Complex c) {
            Complex temp = new Complex(0);
            temp.real = this.real + c.real;
            temp.image = this.image + c.image;
            return temp;
        }
        public Complex SubComplex (Complex c)
        {
            Complex temp = new Complex(0);
            temp.real = this.real - c.real;
            temp.image = this.image - c.image;
            return temp;
        }
        public Complex Mulcomplex(Complex c)
        {
            Complex temp = new Complex(0);
            temp.real = (this.real * c.real - this.image * c.image);
            temp.image = (this.real * c.image + c.real * this.image);
            return temp;
        }
        public Complex DivComplex(Complex c)
        {
            Complex temp = new Complex(0);
            temp.real = (this.real * c.real + this.image * c.image) / (c.real)* (c.real)+ (c.image)* (c.image);
            temp.image = (c.real * this.image - this.real * c.image) / (c.real) * (c.real) + (c.image) * (c.image);
            return temp;
        }
    }
    class Test {
        public static void Main() {
            Complex x1 = new Complex(2.0);
            Complex x2 = new Complex(3.0, -1.0);

            Complex temp = new Complex(0);
            temp = x1.AddComplex(x2);
            Console.Write("덧셈: ");
            temp.toString();
            temp = x1.SubComplex(x2);
            Console.Write("뺄셈: ");
            temp.toString();
            temp = x1.Mulcomplex(x2);
            Console.Write("곱셈: ");
            temp.toString();
            temp = x1.DivComplex(x2);
            Console.Write("나눗셈: ");
            temp.toString();
        }
    }
    */
    //4.13번
    /*class Stack {
        private int[] stack;
        int sp = -1;
        public Stack(int size = 100) {
            stack = new int[size];
        }
        public void Push(int data) {
            stack[++sp] = data;
        }
        public int Pop()
        {
            return stack[sp--];
        }
    }
    class Program
    {
        public static void Main()
        {
            Stack stk1 = new Stack();
            int key = 0;
            int Tindex = 0;

            while (true)
            {
                Console.Write("Enter a Number: ");
                key = int.Parse(Console.ReadLine());
                if (key == 0)
                    break;
                stk1.Push(key);
                Tindex++;
            }
            Console.Write("stack: ");
            while (true)
            {
                Console.Write(stk1.Pop() + " ");
                Tindex--;
                if (Tindex == 0)
                    break;

            }
        }
    }*/
    //4.14
    /*class Vector {
        public int[] v;
        public Vector() {
            v = new int[100];
        }
        public Vector(int size)
        {
            v = new int[size];
        }
        static void Swap(ref int x, ref int y) {
            int temp = x;
            x = y;
            y = temp;
        }
        public void Qsort(int left, int right) {
            int pe;
            int i, last;

            if (left >= right) {
                return;
            }
            pe = (left + right) / 2;
            Swap(ref v[left], ref v[pe]);
            last = left;
            for (i = left + 1; i <= right; i++) {
                if (v[i] < v[left])
                    Swap(ref v[++last], ref v[i]);
            }
            Swap(ref v[left], ref v[last]);
            Qsort(left, last - 1);
            Qsort(last+1, right);
        }
    }
    class Program {
        public static void Main() {
            Vector v = new Vector();
            int key= 0;
            int Tindex = 0;

            while (true)
            {
                Console.Write("Enter a Number: ");
                key = int.Parse(Console.ReadLine());
                if (key == 0)
                    break;
                v.v[Tindex++] = key;
            }

            v.Qsort(0, Tindex-1);

            Console.Write("정렬 후: ");
            for (int i = 0; i < Tindex; i++) {
                Console.Write(v.v[i] + " ");
            }
            Console.WriteLine("");
        }
    }*/
    //5.8
    /*abstract class Figure
    {
        public abstract void Area();
        public abstract void Girth();
        public abstract void Draw();
    }
    class Circle : Figure {
        double radius;
        public Circle(double r = 1) {
            radius = r;
        }
        override public void Area() {
            Console.WriteLine("원의 넓이: " + radius * radius  * 3.14);
        }
        override public void Girth()
        {
            Console.WriteLine("원의 둘레: " + 2 * radius  * 3.14);
        }
        override public void Draw()
        {
            Console.WriteLine("Draw Circle");
        }
    }
    class Rect : Figure{
        int x;
        int y;
        public Rect(int line = 1) {
            x = line; y = line;
        }
        public Rect(int line1, int line2)
        {
            x = line1; y = line2;
        }
        override public void Area()
        {
            Console.WriteLine("사각형의 넓이: " + (x * y));
        }
        override public void Girth()
        {
            Console.WriteLine("사각형의 둘레: " + (x + x + y + y));
        }
        override public void Draw()
        {
            Console.WriteLine("Draw Rect");
        }
    }
 
    class Test {
        public static void Main() {
            Circle circle = new Circle();
            Rect rect = new Rect(1,2);
            circle.Draw();
            circle.Area();
            circle.Girth();

            rect.Draw();
            rect.Area();
            rect.Girth();
        }
    }*/
    //5.9
    interface IOperation{
        void Insert(string str);
        string Delete();
        bool Search(string str);
        string GetCurrentElt();
        int NumOfElements();
    }
    class Stack : IOperation {
        int sp = -1;
        int size;
        string[] stack;

        public Stack(int size = 100) {
            this.size = size;
                stack = new string[size];
        }
        public void Insert(string str) {

            if (sp < size)
                stack[++sp] = str;
            else
                Console.WriteLine("스택 초과");
        }
        public string Delete() {
            if (sp != -1)
                return stack[sp--];
            else
            {
                Console.WriteLine("스택 비어있음");
                return null;
            }
        }
        public bool Search(string str) {
            if (sp != -1) {
                for (int i = 0; i < sp+1; i++)
                    if (stack[i] == str)
                        return true;
                return false;
            }
            else {
                Console.WriteLine("스택 비어있음");
                return false;
            }
        }
        public string GetCurrentElt()
        {
            if (sp != -1)
                return stack[sp];
            else
            {
                Console.WriteLine("스택 비어있음");
                return null;
            }
        }
        public int NumOfElements() {
            if (sp != -1)
                return sp + 1;
            else
                return 0;
        }
    }
    class Queue : IOperation
    {
        int front = 0;
        int rear = 0;
        int size;
        string[] queue;

        public Queue(int size = 100)
        {
            this.size = size;
            queue = new string[size];
        }
        public void Insert(string str)
        {

            if (rear < size)
                queue[rear++] = str;
            else
                Console.WriteLine("큐 초과");
        }
        public string Delete()
        {
            if (rear == front)
            {
                Console.WriteLine("큐 비어있음");
                return null;
            }
            else
            {
                return queue[front++];
            }
        }
        public bool Search(string str)
        {
            if (rear == front)
            {
                Console.WriteLine("큐 비어있음");
                return false;
            }
            else
            {
                for (int i = front; i < rear; i++)
                    if (queue[i] == str)
                        return true;
                return false;
            }
        }
        public string GetCurrentElt()
        {
            if (rear == front) {
                Console.WriteLine("큐 비어있음");
                return null;
            }
            else
                return queue[front];
        }
        public int NumOfElements()
        {
            if (rear == front)
                return 0;
            else
                return rear - front;
        }
    }
    class Test {
        public static void Main() {
            Stack sk = new Stack();
            Queue qe = new Queue();

            sk.Insert("stack1");
            sk.Insert("stack2");
            sk.Insert("stack3");
            Console.WriteLine("Delete =" + sk.Delete());
            Console.WriteLine("stack2 Search =" + sk.Search("stack2"));
            Console.WriteLine("stack3 Search =" + sk.Search("stack3"));
            Console.WriteLine("GetCurrentElt =" + sk.GetCurrentElt());
            Console.WriteLine("NumOfElements =" + sk.NumOfElements());

            qe.Insert("queue1");
            qe.Insert("queue2");
            qe.Insert("queue3");
            Console.WriteLine("Delete =" + qe.Delete());
            Console.WriteLine("queue2 Search =" + qe.Search("queue2"));
            Console.WriteLine("queue1 Search =" + qe.Search("queue1"));
            Console.WriteLine("GetCurrentElt =" + qe.GetCurrentElt());
            Console.WriteLine("NumOfElements =" + qe.NumOfElements());

        }
    }
    //5.11
    /*public interface IFigure
    {
        void Area();
        void Girth();
        void Draw();
    }
    class Circle : IFigure
    {
        double radius;
        public Circle(double r = 1)
        {
            radius = r;
        }
        public void Area()
        {
            Console.WriteLine("원의 넓이: " + radius * radius * 3.14);
        }
        public void Girth()
        {
            Console.WriteLine("원의 둘레: " + 2 * radius * 3.14);
        }
        public void Draw()
        {
            Console.WriteLine("Draw Circle");
        }
    }
    class Rect : IFigure
    {
        int x;
        int y;
        public Rect(int line = 1)
        {
            x = line; y = line;
        }
        public Rect(int line1, int line2)
        {
            x = line1; y = line2;
        }
        public void Area()
        {
            Console.WriteLine("사각형의 넓이: " + (x * y));
        }
        public void Girth()
        {
            Console.WriteLine("사각형의 둘레: " + (x + x + y + y));
        }
        public void Draw()
        {
            Console.WriteLine("Draw Rect");
        }
    }

    class Test
    {
        public static void Main()
        {
            Circle circle = new Circle();
            Rect rect = new Rect();
            circle.Draw();
            circle.Area();
            circle.Girth();

            rect.Draw();
            rect.Area();
            rect.Girth();

        }
    }*/
}


//프로퍼티
/*class Properti
{ 
    int a;
    public int A
    {
        get { return a; }
        set { a = value; }
    }
}*/

//2) 연산자 중복 (overloading재정의) : 클래스로만든 연산
//public static Class operator +(Class x){ }

//3) 델리게이트 (함수에 대한 객체)(함수도 객체로 만들어 다른 객체상호작용) : 이벤트와 스레드 처리방법
/*delegate void one(); delegate void two(int i);
class Deleclass{
public void Met1(){}
public void Met2(int i){}
}
public static void Main(){
Deleclass obj = new Deleclass(); 
one d1 = new one(obj.Met1);
two d2 = new two(obj.met2);
}*/
/*extern int f(int); int (*pf)(); pf = f; sum = (*pf)(a,b); (c dpt)
int execute(int(*pf)(int,int), int ,int) {int add int sub;} execute(add,a,b)*/
//4) 이벤트 (핸들(함수) -> 델리게이트)
/*public delegate void MyevenHandler()
/*class eventapp{
public event EventHandler  Myevent; //이벤트 선언

void MyEventHanldler(object sender,EventArgs e){} //이벤트 처리기 작성
public EventApp(){ this.Myevent += new EventHandler(MyEventhandler); } //이벤트 처러기 등록
public void lnvoke(){ if(Myevent != null) Myevent(this, null) } //이벤트 발생

public static void Main(){ new Eventapp().lnovke() }
 }*/
//스레드 
/*main{  시작
         실행 ->스레드.start();     Thread{ 시작
         끝                                 실행
}->순차적이라면 스레드갔다가                끝
   여기에서 종료                    }->여기에서 프로그램완전종료(실행시간줄임)
*/
//제네릭
/*
 class Stack <Type>{
   Stack<Type> st = new Stack<Type>();
}
Stack<int> i;
 */