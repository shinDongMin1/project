public class Test1 {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int mysteriousState = Integer.parseInt(args[0]);
		
		while(true) {
			System.out.print("Who ");
			try {
				System.out.print("is ");
				if (mysteriousState==1)return;
				System.out.print("that ");
				if (mysteriousState==2)break;
				System.out.print("strange ");
				if (mysteriousState==3)continue;
				System.out.print("but kindly ");
				if (mysteriousState==4)
					throw new Error();
				System.out.print("not at all ");
			}finally {
				System.out.print("amusing ");
			} // end try
			System.out.print("yet compelling ");
			break;
		} // end while
		System.out.print("man?");
	} // end main
}


/*
			public static int f(int n) { 	//1의 비트 수를 세는 메소드
		int m;
		for(m = 0; n!=0; n>>=1)
			if((n&1)==1)m++;
		return m;
	}
		System.out.println("number of bits = " + f(037)); //3*8+7 =31 0011 1111
		
	public static int f(int x, int p, int n) {		//p위치에서  n비트를 추출
		return (x >> (p+1-n)) & ~(~0 << n);
	}
			System.out.println(f(0x0C,3,2)); 		// 0000 1100 

		int i = 0;
		String s = new String("string");
		char c='r'; int sw = 0;
		
		while(s.charAt(i) != '\0') {
			if(c == s.charAt(i)) {
				sw = 1;
				System.out.println("Position of " + c + " = " + (i++));
				break;
			}else i++;
			if(sw == 0)
				System.out.println("Not found");
		}
		
		i = 0; sw = 0;
		do{
			if(c == s.charAt(i)) {
				sw = 1;
				System.out.println("Position of " + c + " = " + (i++));
				break;
			}else i++;
			if(sw == 0)
				System.out.println("Not found");
		}while(s.charAt(i) != '\0');
		
		i = 0; sw = 0;
		for(;;) {
			if(s.charAt(i) != '\0') {
				if(c == s.charAt(i)) {
					sw = 1;
					System.out.println("Position of " + c + " = " + (i++));
					break;
				}else i++;
				if(sw == 0)
					System.out.println("Not found");
			}else break;
		}
	
class Ex extends Exception {}
System.out.println("Entering first try block");
try {
	System.out.println("Entering second try block");
	try {
		throw new Ex();
	} finally {
		System.out.println("finally Ex in 2nd try block");
	}
}catch(Ex e) {
	System.out.println("Caught Ex in first try block");
} finally {
	System.out.println("finally Ex in 1st try block");
	
	
	class FinallyClause{
	public int methodA() {
		try {
			return 1;
		}
		catch(Exception e) {return 2;}
	}
	public int methodB() {
		try {
			return 3;
		}
		finally {return 4;}
	}
}	
	
	
		FinallyClause fc = new FinallyClause();
		System.out.println("methodA returns " + fc.methodA());
		System.out.println("methodB returns " + fc.methodB());
		
		
		int mysteriousState = 4; //Integer.parseInt(args[0]);
		
		while(true) {
			System.out.print("Who ");
			try {
				System.out.print("is ");
				if (mysteriousState==1)return;
				System.out.print("that ");
				if (mysteriousState==2)break;
				System.out.print("strange ");
				if (mysteriousState==3)continue;
				System.out.print("but kindly ");
				if (mysteriousState==4)
					throw new Error();
				System.out.print("not at all ");
			}finally {
				System.out.print("amusing");
			} //end try
			System.out.print("yet compelling ");
			break;
		}//end while
		System.out.print("man?");//end main
}*/