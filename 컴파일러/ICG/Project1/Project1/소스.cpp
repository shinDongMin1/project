#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
// 파일을 참조
#include "miniC.tbl"
// 키워드는 7개
#define NO_KEYWORDS 7
// 문자의 최대 길이는 12
#define ID_LENGTH 12
// 스택의 사이즈
#define PS_SIZE 200

// 토큰에 대한 정보를 가진 구조체
struct tokenType {
    int number;  // token number
    union {
        char id[ID_LENGTH];
        int num;
    } value;  // token value
};

// 임시로 문자를 받을 공간
char id[ID_LENGTH];

// 노드에 대한 정보를 가진 구조체
enum noderep { terminal, nonterm };
typedef struct nodetype {
    struct tokenType token;
    enum noderep noderep;
    struct nodetype* son;
    struct nodetype* brother;
}NODE;

// 에러 카운트, 스택에 대한 포인터, 상태스택, 심벌스택, 노드스택
int errcnt = 0, sp, stateStack[PS_SIZE], symbolStack[PS_SIZE];
NODE* valueStack[PS_SIZE];

// 심벌테이블에 사용되는 함수
void emitSym(int base, int offset, int size);

// 심벌테이블과 함수들 참조
#include "SymTab.c"

// 소스파일, AST파일, U-code파일
FILE* source_file;
FILE* astFile;
FILE* ucodeFile;

// ICG에 대한 변수들 선언
int lvalue, rvalue, labelNum = 0, width = 1, stTop, symLevel = 0;

/* ********************** scanner ********************** */

//인식할 수 있는 심벌들
enum tsymbol {
    tnull = -1,
    /*  0   1   2   3   4   5  */
    tnot, tnotequ, tmod, tmodAssign, tident, tnumber,
    /*  6   7   8   9   10  11  */
    tand, tlparen, trparen, tmul, tmulAssign, tplus,
    /*  12  13  14  15  16  17  */
    tinc, taddAssign, tcomma, tminus, tdec, tsubAssign,
    /*  18  19  20  21  22  23  */
    tdiv, tdivAssign, tsemicolon, tless, tlesse, tassign,
    /*  24  25  26  27  28  29  */
    tequal, tgreat, tgreate, tlbracket, trbracket, teof,

    // 키워드 7개
    /*  30  31  32  33  34  35  36 */
    tconst, telse, tif, tint, treturn, tvoid, twhile,
    /*  37  38  39  */
    tlbrace, tor, trbrace
};

// 이진탐색으로 찾을 키워드 7개
const char* keyword[] = {
    "const", "else", "if", "int", "return", "void", "while"
};

// 이진탐색으로 찾은 키워드의 token number 배정할때 사용
enum tsymbol tnum[] = {
    tconst, telse, tif, tint, treturn, tvoid, twhile
};

// 발생할 수 있는 에러 함수
void lexicalError(int n)
{
    printf(" *** Lexical Error : ");
    switch (n) {
    // 12 자를 넘김
    case 1: printf("an identifier length must be less than 12.\n");
        break;
    // & 다음으로 &이 아닌 다른 문자가 올때
    case 2: printf("next character must be &.\n");
        break;
    // | 다음으로 |이 아닌 다른 문자가 올때
    case 3: printf("next character must be |.\n");
        break;
    // 인식할 수 없음
    case 4: printf("invalid character!!!\n");
        break;
    }
}

// 첫글자가 문자인지 확인하는 함수
int superLetter(char ch)
{
    if (isalpha(ch) || ch == '_') return 1;
    else return 0;
}

// 글자가 문자나 숫자인지 확인하는 함수
int superLetterOrDigit(char ch)
{
    if (isalnum(ch) || ch == '_') return 1;
    else return 0;
}

// 문자로 읽은 숫자값을 상수로 변환하는 함수 
int getIntNum(char firstCharacter, FILE* source_file)
{
    int num = 0;
    char ch;
    ch = firstCharacter;

    // 상수로 변환하는 반복문
    do {
        num = 10 * num + (int)(ch - '0');
        ch = fgetc(source_file);
    } while (isdigit(ch)); // 숫자가 아닐때까지 반복

    ungetc(ch, source_file); // retract
    return num;
}

// 파일을 받아 토큰을 찾는 함수
struct tokenType scanner(FILE* source_file)
{
    struct tokenType token;
    int i, j, k;
    char ch;
    token.number = tnull;
   
    do {
        // state 1: 공백제거
        while (isspace(ch = fgetc(source_file)));
        i = 0;
        // 첫 글자가 문자면
        if (superLetter(ch)) { 
            // 글자를 임시로 저장
            do {
                if (i < ID_LENGTH) id[i++] = ch;
                ch = fgetc(source_file);
            } while (superLetterOrDigit(ch)); // 문자나 숫자가 아닐때까지
            if (i >= ID_LENGTH) lexicalError(1);
            id[i] = '\0';
            ungetc(ch, source_file); // retract

            // 이진탐색: find the identifier in the keyword table
            i = 0;
            j = NO_KEYWORDS - 1;
            do {
                k = (i + j) / 2;
                if (strcmp(id, keyword[k]) >= 0) i = k + 1;
                if (strcmp(id, keyword[k]) <= 0) j = k - 1;
            } while (i <= j);
            // found, keyword exit
            if ((i - 1) > j) { // state 4 : keyword
                token.number = tnum[k];
                strcpy(token.value.id, id);
                //strcpy(token.tokenValue, id);
            }
            // not found, identifier exit
            else { // state 3 : identifier
                token.number = tident;
                strcpy(token.value.id, id);
                //strcpy(token.tokenValue, id);
            }
        }// end of identifier or keyword

        // 첫 글자가 숫자면
        else if (isdigit(ch)) {
            token.number = tnumber;
            token.value.num = getIntNum(ch, source_file);
            //token.tokenValue = getIntNum(ch, source_file);
        }

        // 구분자, 연산자를 구분
        else {
            //token.value.id[i++] = ch;
            switch (ch) {
            case '/':     // state 10
                ch = fgetc(source_file);
                if (ch == '*') {  // text comment
                    ch = fgetc(source_file);
                    do {
                        while (ch != '*') ch = fgetc(source_file);
                        ch = fgetc(source_file);
                    } while (ch != '/');
                }
                else if (ch == '/')  // line comment
                    while (fgetc(source_file) != '\n');
                else if (ch == '=') { token.number = tdivAssign; //token.value.id[i++] = ch; 
                }
                else {
                    token.number = tdiv;
                    ungetc(ch, source_file); // retract
                }
                break;
            case '!':     // state 17
                ch = fgetc(source_file);
                if (ch == '=') { token.number = tnotequ; //token.value.id[i++] = ch; 
                }
                else {
                    token.number = tnot;
                    ungetc(ch, source_file); // retract
                }
                break;
            case '%':     // state 20
                ch = fgetc(source_file);
                if (ch == '=') { token.number = tmodAssign; //token.value.id[i++] = ch; 
                }
                else {
                    token.number = tmod;
                    ungetc(ch, source_file);
                }
                break;

            case '&':     // state 23
                ch = fgetc(source_file);
                if (ch == '&') { token.number = tand; //token.value.id[i++] = ch; 
                }
                else {
                    lexicalError(2);
                    ungetc(ch, source_file); // retract
                }
                break;
            case '*':     // state 25
                ch = fgetc(source_file);
                if (ch == '=') { token.number = tmulAssign; //token.value.id[i++] = ch; 
                }
                else {
                    token.number = tmul;
                    ungetc(ch, source_file); // retract
                }
                break;
            case '+':     // state 28
                ch = fgetc(source_file);
                if (ch == '+') { token.number = tinc; //token.value.id[i++] = ch; 
                }
                else if (ch == '=') { token.number = taddAssign; //token.value.id[i++] = ch; 
                }
                else {
                    token.number = tplus;
                    ungetc(ch, source_file); // retract
                }
                break;
            case '-':     // stats 32
                ch = fgetc(source_file);
                if (ch == '-') { token.number = tdec; //token.value.id[i++] = ch; 
                }
                else if (ch == '=') { token.number = tsubAssign; //token.value.id[i++] = ch;
                }
                else {
                    token.number = tminus;
                    ungetc(ch, source_file); // retract
                }
                break;
            case '<':     // state 36
                ch = fgetc(source_file);
                if (ch == '=') { token.number = tlesse; //token.value.id[i++] = ch; 
                }
                else {
                    token.number = tless;
                    ungetc(ch, source_file); // retract
                }
                break;
            case '=':     // state 39
                ch = fgetc(source_file);
                if (ch == '=') { token.number = tequal; //token.value.id[i++] = ch;
                }
                else {
                    token.number = tassign;
                    ungetc(ch, source_file); // retract
                }
                break;
            case '>':     // state 42
                ch = fgetc(source_file);
                if (ch == '=') { token.number = tgreate; //token.value.id[i++] = ch; 
                }
                else {
                    token.number = tgreat;
                    ungetc(ch, source_file); // retract
                }
                break;
            case '|':     // state 45
                ch = fgetc(source_file);
                if (ch == '|') { token.number = tor; //token.value.id[i++] = ch;
                }
                else {
                    lexicalError(3);
                    ungetc(ch, source_file); // retract
                }
                break;
            // 구분자와 파일의 끝
            case '(': token.number = tlparen;   break;
            case ')': token.number = trparen;   break;
            case ',': token.number = tcomma;    break;
            case ';': token.number = tsemicolon;    break;
            case '[': token.number = tlbracket; break;
            case ']': token.number = trbracket; break;
            case '{': token.number = tlbrace;   break;
            case '}': token.number = trbrace;   break;
            case EOF: token.number = teof;  break;
            // 이곳에도 없다면 인식할 수 없는 글자
            default: {
                printf("Current character : %c", ch);
                lexicalError(4);
                break;
            }
            } // end of switch
            //token.value.id[i] = '\0';
        }// end of else
    } while (token.number == tnull); //토큰을 찾을때까지 반복
    //찾은 토큰 반환
    return token;
} // end of scanner

/* ************************ AST ************************ */

// 노드들의 이름들
const char* nodeName[] = {
    "ACTUAL_PARAM",   "ADD",            "ADD_ASSIGN",     "ARRAY_VAR",      "ASSIGN_OP",
    "CALL",           "COMPOUND_ST",    "CONST_NODE",     "DCL",            "DCL_ITEM",
    "DCL_LIST",       "DCL_SPEC",       "DIV",            "DIV_ASSIGN",     "EQ",
    "ERROR_NODE",     "EXP_ST",         "FORMAL_PARA",    "FUNC_DEF",       "FUNC_HEAD",
    "GE",             "GT",             "IDENT",          "IF_ELSE_ST",     "IF_ST",
    "INDEX",          "INT_NODE",       "LE",             "LOGICAL_AND",    "LOGICAL_NOT",
    "LOGICAL_OR",     "LT",             "MOD",            "MOD_ASSIGN",     "MUL",
    "MUL_ASSIGN",     "NE",             "NUMBER",         "PARAM_DCL",      "POST_DEC",
    "POST_INC",       "PRE_DEC",        "PRE_INC",        "PROGRAM",        "RETURN_ST",
    "SIMPLE_VAR",     "STAT_LIST",      "SUB",            "SUB_ASSIGN",     "UNARY_MINUS",
    "VOID_NODE",      "WHILE_ST"
};

// 노드들의 이름마다 열거값을 지정
enum nodeNumber
{
    ACTUAL_PARAM, ADD, ADD_ASSIGN, ARRAY_VAR, ASSIGN_OP,
    CALL, COMPOUND_ST, CONST_NODE, DCL, DCL_ITEM,
    DCL_LIST, DCL_SPEC, DIV, DIV_ASSIGN, EQ,
    ERROR_NODE, EXP_ST, FORMAL_PARA, FUNC_DEF, FUNC_HEAD,
    GE, GT, IDENT, IF_ELSE_ST, IF_ST,
    INDEX, INT_NODE, LE, LOGICAL_AND, LOGICAL_NOT,
    LOGICAL_OR, LT, MOD, MOD_ASSIGN, MUL,
    MUL_ASSIGN, NE, NUMBER, PARAM_DCL, POST_DEC,
    POST_INC, PRE_DEC, PRE_INC, PROGRAM, RETURN_ST,
    SIMPLE_VAR, STAT_LIST, SUB, SUB_ASSIGN, UNARY_MINUS,
    VOID_NODE, WHILE_ST
};

// 트리를 만들때 넣는 노드넘버들
int ruleName[] = {
    /* 0               1               2               3               4           */
    0,              PROGRAM,        0,              0,              0,
    /* 5               6               7               8               9           */
    0,              FUNC_DEF,       FUNC_HEAD,      DCL_SPEC,       0,
    /* 10              11              12              13              14          */
    0,              0,              0,              CONST_NODE,     INT_NODE,
    /* 15              16              17              18              19          */
    VOID_NODE,      0,              FORMAL_PARA,    0,              0,
    /* 20              21              22              23              24          */
    0,              0,              PARAM_DCL,      COMPOUND_ST,    DCL_LIST,
    /* 25              26              27              28              29          */
    DCL_LIST,       0,              0,              DCL,            0,
    /* 30              31              32              33              34          */
    0,              DCL_ITEM,       DCL_ITEM,       SIMPLE_VAR,     ARRAY_VAR,
    /* 35              36              37              38              39          */
    0,              0,              STAT_LIST,      0,              0,
    /* 40              41              42              43              44          */
    0,              0,              0,              0,              0,
    /* 45              46              47              48              49          */
    0,              EXP_ST,         0,              0,              IF_ST,
    /* 50              51              52              53              54          */
    IF_ELSE_ST,     WHILE_ST,       RETURN_ST,      0,              0,
    /* 55              56              57              58              59          */
    ASSIGN_OP,      ADD_ASSIGN,     SUB_ASSIGN,     MUL_ASSIGN,     DIV_ASSIGN,
    /* 60              61              62              63              64          */
    MOD_ASSIGN,     0,              LOGICAL_OR,     0,              LOGICAL_AND,
    /* 65              66              67              68              69          */
    0,              EQ,             NE,             0,              GT,
    /* 70              71              72              73              74          */
    LT,             GE,             LE,             0,              ADD,
    /* 75              76              77              78              79          */
    SUB,            0,              MUL,            DIV,            MOD,
    /* 80              81              82              83              84          */
    0,              UNARY_MINUS,    LOGICAL_NOT,    PRE_INC,        PRE_DEC,
    /* 85              86              87              88              89          */
    0,              INDEX,          CALL,           POST_INC,       POST_DEC,
    /* 90              91              92              93              94          */
    0,              0,              ACTUAL_PARAM,   0,              0,
    /* 95              96              97                                          */
    0,              0,              0
};

// shift action일때 명칭이나 상수이면 노드를 생성하는 함수
NODE* buildNode(struct tokenType token) {
    NODE* ptr;
    ptr = (NODE*)malloc(sizeof(NODE));
    if (!ptr) {
        printf("bulid node malloc error\n");
        exit(1);
    }
    ptr->token = token;
    ptr->noderep = terminal;
    ptr->son = NULL;
    ptr->brother = NULL;
    return ptr;
}

// reduce action일때 서브 트리를 생성하는 함수
NODE* buildTree(int nodeNumber, int rhsLength) {
    int i, j, start;
    NODE* first, * ptr;

    i = sp - rhsLength + 1;

    // step 1: find a first index with node in value stack
    while (i <= sp && valueStack[i] == NULL) i++;
    if (!nodeNumber && i > sp) return NULL;
    start = i;

    // step 2: linking brothers
    while (i <= sp - 1) {
        j = i + 1;
        while (j <= sp && valueStack[j] == NULL) j++;
        if (j <= sp) {
            ptr = valueStack[i];
            while (ptr->brother) ptr = ptr->brother;
            ptr->brother = valueStack[j];
        }
        i = j;
    }
    first = (start > sp) ? NULL : valueStack[start];

    // step 3: making subtree root and linking son
    if (nodeNumber) {
        ptr = (NODE*)malloc(sizeof(NODE));
        if (!ptr) {
            printf("malloc error in buildTree()\n");
            exit(1);
        }
        ptr->token.number = nodeNumber;
        ptr->noderep = nonterm;
        ptr->son = first;
        ptr->brother = NULL;
        return ptr;
    }
    else return first;
}

// 노드를 출력하는 함수
void printNode(NODE* pt, int indent) {
    int i;

    for (i = 1; i <= indent; i++) {
        fprintf(astFile, " ");
    }
    if (pt->noderep == terminal) { // terminal node
        if (pt->token.number == tident) {
            fprintf(astFile, " Terminal: %s", pt->token.value.id);
        }
        else if (pt->token.number == tnumber) {
            fprintf(astFile, " Terminal: %d", pt->token.value.num);
        }
    }
    else { // nonterminal node
        int i;
        i = (int)(pt->token.number);
        fprintf(astFile, " Nonterminal: %s", nodeName[i]);
    }
    fprintf(astFile, "\n");
}

// 트리형태로 출력하는 함수
void printTree(NODE* pt, int indent) {
    NODE* p = pt;
    while (p != NULL)
    {
        printNode(p, indent);
        if (p->noderep == nonterm) printTree(p->son, indent + 5);
        p = p->brother;
    }
}

// 명칭이나 상수인지 확인하는 함수
int meaningfulToken(struct tokenType token) {
    if ((token.number == tident) || (token.number == tnumber))
        return 1;
    else return 0;
}

/* ********************** parser ********************** */

// 토큰의 이름들
const char* tokenName[] = {
  /* 0       1        2       3         4            5       */
    "!",    "!=",    "%",    "%=",   "%ident",    "%number",
  /* 6       7        8       9         10           11      */
    "&&",   "(",     ")",    "*",      "*=",        "+",
  /* 12      13       14      15        16           17      */
    "++",   "+=",    ",",    "-",      "--",        "-=",
  /* 18      19       20      21        22           23      */
    "/",    "/=",    ";",    "<",      "<=",        "=",
  /* 24      25       26      27        28           29      */
    "==",   ">",     ">=",   "[",      "]",         "eof",
  // .................... word symbol ...................... //
  /* 30      31       32      33        34           35        36     */
  "const",  "else",  "if",   "int",    "return",    "void",   "while",
  /* 37      38       39                                    */
    "{",    "||",    "}"
};

// reduce했을 때 rule넘버를 출력하는 함수
void semantic(int n) {
    printf("reduce rule number = %d\n", n);
}

// token을 받아 알맞은 형태로 출력하는 함수
void printToken(struct tokenType token) {
    if(token.number == tident)
        printf("%s\n", token.value.id);
    else if (token.number == tnumber)
        printf("%d\n", token.value.num);
    else
        printf("%s\n", tokenName[token.number]);
}

// 스택을 채웠는데 에러가 있을 시 비워주는 함수
void dumpStack() {
    int i, start;

    if (sp > 10) start = sp - 10;
    else start = 0;

    printf("\n *** dump state stack :");
    for(i=start; i <= sp; ++i)
        printf(" %d", stateStack[i]);

    printf("\n *** dump symbol stack :");
    for (i = start; i <= sp; ++i)
        printf(" %d", symbolStack[i]);
    printf("\n");
}

// 에러에 대한 토큰과 상태 스택을 조정하는 함수
void errorRecovery(FILE* source_file) {
    struct tokenType tok;
    int parenthesisCount, braceCount;
    int i;
    // step1: skip to the semicolon
    parenthesisCount = braceCount = 0;
    while (true)
    {
        tok = scanner(source_file);
        if (tok.number == teof) exit(1);

        if (tok.number == tlparen) parenthesisCount++;
        else if (tok.number == trparen) parenthesisCount--;

        if (tok.number == tlbrace) braceCount++;
        else if (tok.number == trbrace) braceCount--;

        if ((tok.number == tsemicolon) && (parenthesisCount <= 0) && (braceCount <= 0))
            break;
    }
    // step2: adjust state stack
    for (i = sp; i >= 0; i--) {
        // statement_list -> statement_list . statement
        if (stateStack[i] == 36) break; //second statement part

        // statement_list -> . statement
        // statement_list -> . statement_list statement
        if (stateStack[i] == 24) break; //first statement part

        // declaration_list -> declaration_list . declaration
        if (stateStack[i] == 25) break; //second internal dcl

        // declaration_list -> . declaration
        // declaration_list -> . declaration_list declaration
        if (stateStack[i] == 17) break; //internal declaration

        // external declaration
        // external_dcl -> . declaration
        if (stateStack[i] == 2) break; //after first external dcl
        if (stateStack[i] == 0) break; //first external declaration
    }
    sp = i;
}

// 파일을 받아 현재 상태에 대한 토큰마다 테이블에서 값을 찾아 action을 정해서 파싱하는 함수
NODE* parser(FILE* source_file) {
    // miniC.tbl파일에 있는 외부 변수
    extern int parsingTable[NO_STATES][NO_SYMBOLS + 1];
    extern int leftSymbol[NO_RULES + 1], rightLength[NO_RULES + 1];

    int entry, rulenumber, lhs;
    int currentState;
    struct tokenType token;
    NODE* ptr;

    sp = 0; stateStack[sp] = 0; // 초기 상태
    token = scanner(source_file);

    while (true)
    {
        currentState = stateStack[sp]; // 현재 상태
        entry = parsingTable[currentState][token.number]; // 상태에 대한 어떤 토큰이 왔는지를 테이블에서 다음 규칙값으로 찾아 저장
        if (entry > 0) {    // 1.shift action
            sp++;
            if (sp > PS_SIZE) {     // 스택의 범위를 벗어나면 에러  
                printf("critical compiler error: parsing stack overflew");
                exit(1);
            }
            symbolStack[sp] = token.number;
            stateStack[sp] = entry;
            valueStack[sp] = meaningfulToken(token) ? buildNode(token) : NULL;
            token = scanner(source_file);
        }
        else if (entry < 0) {   // 2.reduce action
            rulenumber = -entry;
            if (rulenumber == GOAL_RULE) {  // 3.accept action
                if (errcnt == 0) return valueStack[sp - 1];//printf(" *** valid source ***\n"); // GOAL_RULE까지 에러가 없으면 파싱 종료
                else printf(" *** error in source: %d\n", errcnt);  // 카운트가 되었으면 에러
            
            }
            //semantic(rulenumber);   // reduce를 알림
            ptr = buildTree(ruleName[rulenumber], rightLength[rulenumber]);
            sp = sp - rightLength[rulenumber];  // reduce되었으니 스택에서 그만큼 길이를 제거 
            lhs = leftSymbol[rulenumber];   // non-terminer인 왼쪽 심벌로 대체
            currentState = parsingTable[stateStack[sp]][lhs]; // 대체된 것에 대한 새로운 상태
            sp++;
            symbolStack[sp] = lhs;
            stateStack[sp] = currentState;
            valueStack[sp] = ptr;
        }
        else {  // 4.error action
            printf(" === error in source ===\n");
            errcnt++;
            printf("Current Token : ");
            printToken(token);  // 에러가 난 현재 토큰 출력
            dumpStack();    // 에러에 대한 스택 비움
            errorRecovery(source_file); // 에러에 대한 회복
            token = scanner(source_file);
        }
    }
}

/* ********************** ICG ********************** */

// 연산자들의 이름마다 열거값을 지정
enum opcodeEnum {
    notop, neg, incop, decop, dup,
    add, sub, mult, divop, modop, swp,
    andop, orop, gt, lt, ge, le, eq, ne,
    lod, str, ldc, lda,
    ujp, tjp, fjp,
    chkh, chkl,
    ldi, sti,
    call, ret, retv, ldp, proc, endop,
    nop, bgn, sym
};

// 연산자들의 이름들
const char* opcodeName[] = {
    "notop",    "neg",	"inc",	"dec",	"dup",
    "add",	"sub",	"mult",	"div",	"mod",	"swp",
    "and",	"or",	"gt",	"lt",	"ge",	"le",	"eq",	"ne",
    "lod",	"str",	"ldc",	"lda",
    "ujp",	"tjp",	"fjp",
    "chkh",	"chkl",
    "ldi",	"sti",
    "call",	"ret",	"retv",	"ldp",	"proc",	"end",
    "nop",	"bgn",	"sym"
};

// ICG에서 에러를 출력하는 함수
void icg_error(int num)
{
    printf("ICG_ERROR: %d\n", num);
}

// 연산자만 있을 경우를 출력하는 함수
void emit0(const char* value) {
    fprintf(ucodeFile, "           %s\n", value);
    printf("           %s\n", value);
}

// 연산자와 1개에 비연산자가 있을 경우를 출력하는 함수
void emit1(const char* value, int p) {
    fprintf(ucodeFile, "           %s  %d\n", value, p);
    printf("           %s  %d\n", value, p);
}

// 연산자와 2개에 비연산자가 있을 경우를 출력하는 함수
void emit2(const char* value, int p, int q) {
    fprintf(ucodeFile, "           %s  %d  %d\n", value, p, q);
    printf("           %s  %d  %d\n", value, p, q);
}

// 지정 label로 이동하는 경우를 출력하는 함수
void emitJump(const char* value, const char* label) {
    fprintf(ucodeFile, "           %s  %s\n", value, label);
    printf("           %s  %s\n", value, label);
}

// 지정 label를 출력하는 함수
void emitLabel(const char* label) {
    fprintf(ucodeFile, "%s nop\n", label);
    printf("%s nop\n", label);
}

// 비연산자들 중에 연산에 필요한 값을 읽는 함수
void rv_emit(NODE* ptr)
{
    int stIndex;

    if (ptr->token.number == tnumber)
        emit1("ldc", ptr->token.value.num);
    else {
        stIndex = lookup(ptr->token.value.id);
        if (stIndex == -1) return;

        if (symbolTable[stIndex].typeQualifier == CONST_TYPE)	// constant
            emit1("ldc", symbolTable[stIndex].initialValue);
        else if (symbolTable[stIndex].width > 1) {	            // array var
            emit2("lda", symbolTable[stIndex].base, symbolTable[stIndex].offset);
        }
        else													// simple var
            emit2("lod", symbolTable[stIndex].base, symbolTable[stIndex].offset);    
    }
}

// 변수를 선언하는 sym을 만드는 함수
void emitSym(int base, int offset, int size) {
    fprintf(ucodeFile, "           %s  %d  %d  %d\n", "sym", base, offset, size);
    printf("           %s  %d  %d  %d\n", "sym", base, offset, size);

}

// label를 만드는 함수
void genLabel(char* label) {

    sprintf(label, "$$%-8d", labelNum++);
}

// 변수에 대한 타입을 확인하는 함수
int typeSize(int typeSpecifier)
{
    if (typeSpecifier == INT_TYPE)
        return 1;
    else {
        printf("not yet implemented\n");
        return 1;
    }
}

// 단순 변수인지 확인하고 맞다면 심벌테이블에 저장하는 함수
void processSimpleVariable(NODE* ptr, int typeSpecifier, int typeQualifier)
{
    NODE* p = ptr->son;     // variable name(=> identifier)
    NODE* q = ptr->brother; // initial value part
    int stIndex, size, initialValue;
    int sign = 1;

    if (ptr->token.number != SIMPLE_VAR) printf("error in SIMPLE_VAR\n");

    if (typeQualifier == CONST_TYPE) {   // constant type
        if (q == NULL) {
            printf("%s must have a constant value\n", ptr->son->token.value.id);
            return;
        }
        if (q->token.number == UNARY_MINUS) {
            sign = -1;
            q = q->son;
        }
        initialValue = sign * q->token.value.num;

        stIndex = insert(p->token.value.id, typeSpecifier, typeQualifier,
            0/*base*/, 0/*offset*/, 0/*width*/, initialValue);
    }
    else {
        size = typeSize(typeSpecifier);
        stIndex = insert(p->token.value.id, typeSpecifier, typeQualifier, base, offset, width, 0);
        offset += size;
    }
}

// 배열 변수인지 확인하고 맞다면 심벌테이블에 저장하는 함수
void processArrayVariable(NODE* ptr, int typeSpecifier, int typeQualifier)
{
    NODE* p = ptr->son; // variable name(=> identifier)
    int stIndex, size;

    if (ptr->token.number != ARRAY_VAR) {
        printf("error in ARRAY_VAR\n");
        return;
    }
    if (p->brother == NULL) // no size
        printf("array size must be specified\n");
    else size = p->brother->token.value.num;

    size *= typeSize(typeSpecifier);

    stIndex = insert(p->token.value.id, typeSpecifier, typeQualifier,
        base, offset, size, 0);
    offset += size;
}

// 선언을 위해서 어떤 변수인지 구분하는 함수
void processDeclaration(NODE* ptr)
{
    int typeSpecifier, typeQualifier;
    NODE* p, * q;

    if (ptr->token.number != DCL_SPEC) icg_error(4);

    // printf("processDeclaration\n");
    // step 1: process DCL_SPEC
    typeSpecifier = INT_TYPE; // default type
    typeQualifier = VAR_TYPE;
    p = ptr->son;
    while (p) {
        if (p->token.number == INT_NODE) typeSpecifier = INT_TYPE;
        else if (p->token.number == CONST_NODE)
            typeQualifier = CONST_TYPE;
        else { // AUTO, EXTERN, REGISTER, FLOAT, DOUBLE, SIGNED, UNSIGEND
            printf("not yet implemented\n");
            return;
        }
        p = p->brother;
    }

    // step 2: process DCL_ITEM
    p = ptr->brother;
    if (p->token.number != DCL_ITEM) icg_error(5);

    while (p) {
        q = p->son; // SIMPLE_VAR or ARRAY_VAR
        switch (q->token.number) {
        case SIMPLE_VAR: // simple variable
            processSimpleVariable(q, typeSpecifier, typeQualifier);
            break;
        case ARRAY_VAR:  // array variable
            processArrayVariable(q, typeSpecifier, typeQualifier);
            break;
        default:
            printf("error in SIMPLE_VAR or ARRAY_VAR\n");
            break;
        }
        p = p->brother;
    }
}

void processOperator(NODE* ptr);
// if, read, write를 call로 부르는 경우를 출력하는 함수
int checkPredefined(NODE* ptr) {
    NODE* p = ptr;
    char* functionName;
    int noArguments;
    int stIndex;

    functionName = p->token.value.id;

    if (strcmp("read", p->token.value.id) == 0) // read를 call했을 때
    {
        noArguments = 1;

        emit0("ldp");
        p = p->brother; // ACTUAL_PARAM
        while (p)
        {
            if (p->noderep == nonterm)
            {
                processOperator(p);
            }
            else {
                stIndex = lookup(p->token.value.id);
                if (stIndex == -1)
                {
                    break;
                }
                emit2("lda", symbolTable[stIndex].base, symbolTable[stIndex].offset);
            }
            noArguments--;
            p = p->brother;
        }

        if (noArguments > 0)
        {
            printf("%s: too few actual arguments\n", functionName);
        }

        if (noArguments < 0)
        {
            printf("%s: too many actual arguments\n", functionName);
        }

        emitJump("call", functionName);
        return 1;
    }
    else if (strcmp("write", p->token.value.id) == 0)   // write를 call했을 때
    {
        noArguments = 1;

        emit0("ldp");
        p = p->brother; // ACTUAL_PARAM
        while (p)
        {
            if (p->noderep == nonterm)
                processOperator(p);
            else {
                stIndex = lookup(p->token.value.id);
                if (stIndex == -1) break;;
                emit2("lod", symbolTable[stIndex].base, symbolTable[stIndex].offset);
            }
            noArguments--;
            p = p->brother;
        }

        if (noArguments > 0)
        {
            printf("%s: too few actual arguments\n", functionName);
        }

        if (noArguments < 0)
        {
            printf("%s: too many actual arguments\n", functionName);
        }
        emitJump("call", functionName);
        return 1;
    }
    else if (strcmp(functionName, "lf") == 0)   // lf를 call했을 때
    {
        emitJump("call", functionName);
        return 1;
    }

    return 0;
}

// 연산자들을 처리하는 함수
void processOperator(NODE* ptr)
{
    switch (ptr->token.number) {
        // assignment operator
    case ASSIGN_OP:
    {
        NODE* lhs = ptr->son, * rhs = ptr->son->brother;
        int stIndex;

        // step 1: generate instructions for left-hand side if INDEX node.
        if (lhs->noderep == nonterm) { // array variable
            lvalue = 1;
            processOperator(lhs);
            lvalue = 0;
        }

        // step 2: generate instructions for right-hand side
        if (rhs->noderep == nonterm) processOperator(rhs);
        else rv_emit(rhs);

        // step 3: generate a store instruction
        if (lhs->noderep == terminal) { // simple variable
            stIndex = lookup(lhs->token.value.id);
            if (stIndex == -1) {
                printf("undefined variable : %s\n", lhs->token.value.id);
                return;
            }
            emit2("str", symbolTable[stIndex].base, symbolTable[stIndex].offset);
        }
        else
            emit0("sti");
        break;
    }

    // complex assignment operators
    case ADD_ASSIGN: case SUB_ASSIGN: case MUL_ASSIGN:
    case DIV_ASSIGN: case MOD_ASSIGN:
    {
        NODE* lhs = ptr->son, * rhs = ptr->son->brother;
        int nodeNumber = ptr->token.number;
        int stIndex;

        ptr->token.number = ASSIGN_OP;
        // step 1: code generation for left hand side
        if (lhs->noderep == nonterm) {
            lvalue = 1;
            processOperator(lhs);
            lvalue = 0;
        }
        ptr->token.number = nodeNumber;
        // step 2: code generation for repeating part
        if (lhs->noderep == nonterm)
            processOperator(lhs);
        else rv_emit(lhs);
        // step 3: code generation for right hand side
        if (rhs->noderep == nonterm)
            processOperator(rhs);
        else rv_emit(rhs);
        // step 4: emit the corresponding operation code
        switch (ptr->token.number) {
        case ADD_ASSIGN: emit0("add"); break;
        case SUB_ASSIGN: emit0("sub"); break;
        case MUL_ASSIGN: emit0("mult"); break;
        case DIV_ASSIGN: emit0("div"); break;
        case MOD_ASSIGN: emit0("mod"); break;
        }
        // step 5: code generation for store code
        if (lhs->noderep == terminal) {
            stIndex = lookup(lhs->token.value.id);
            if (stIndex == -1) {
                printf("undefined variable : %s\n", lhs->son->token.value.id);
                return;
            }
            emit2("str", symbolTable[stIndex].base, symbolTable[stIndex].offset);
        }
        else
            emit0("sti");
        break;
    }

    // binary(arithmetic/relational/logical) operators
    case ADD: case SUB: case MUL: case DIV: case MOD:
    case EQ: case NE: case GT: case LT: case GE: case LE:
    case LOGICAL_AND: case LOGICAL_OR:
    {
        NODE* lhs = ptr->son, * rhs = ptr->son->brother;

        // step 1: visit left operand
        if (lhs->noderep == nonterm) processOperator(lhs);
        else rv_emit(lhs);
        // step 2: visit right operand
        if (rhs->noderep == nonterm) processOperator(rhs);
        else rv_emit(rhs);
        // step 3: visit root
        switch (ptr->token.number) {
        case ADD: emit0("add"); break;            // arithmetic operators
        case SUB: emit0("sub"); break;
        case MUL: emit0("mult"); break;
        case DIV: emit0("div"); break;
        case MOD: emit0("mod"); break;
        case EQ: emit0("eq"); break;              // relational operators
        case NE: emit0("ne"); break;
        case GT: emit0("gt"); break;
        case LT: emit0("lt"); break;
        case GE: emit0("ge"); break;
        case LE: emit0("le"); break;
        case LOGICAL_AND: emit0("and"); break;  // logical operators
        case LOGICAL_OR: emit0("or"); break;
        }
        break;
    }

    // unary operators
    case UNARY_MINUS: case LOGICAL_NOT:
    {
        NODE* p = ptr->son;

        if (p->noderep == nonterm) processOperator(p);
        else rv_emit(p);
        switch (ptr->token.number) {
        case UNARY_MINUS: emit0("neg"); break;
        case LOGICAL_NOT: emit0("not"); break;
        }
        break;
    }

    // increment/decrement operators
    case PRE_INC: case PRE_DEC: case POST_INC: case POST_DEC:
    {
        NODE* p = ptr->son; NODE* q;
        int stIndex; // int amount = 1;
        if (p->noderep == nonterm) processOperator(p); // compute operand
        else rv_emit(p);

        q = p;
        while (q->noderep != terminal) q = q->son;
        if (!q || (q->token.number != tident)) {
            printf("increment/decrement operators can not be applied in expression\n");
            return;
        }
        stIndex = lookup(q->token.value.id);
        if (stIndex == -1) return;

        switch (ptr->token.number) {
        case PRE_INC:
            emit0("inc");
            // if(isOperation(ptr)) emit0(dup);
            break;
        case PRE_DEC:
            emit0("dec");
            // if(isOperation(ptr)) emit0(dup);
            break;
        case POST_INC:
            // if(isOperation(ptr)) emit0(dup);
            emit0("inc");
            break;
        case POST_DEC:
            // if(isOperation(ptr)) emit0(dup);
            emit0("dec");
            break;
        }
        if (p->noderep == terminal) {
            stIndex = lookup(p->token.value.id);
            if (stIndex == -1) return;
            emit2("str", symbolTable[stIndex].base, symbolTable[stIndex].offset);
        }
        else if (p->token.number == INDEX) { // compute index
            lvalue = 1;
            processOperator(p);
            lvalue = 0;
            emit0("swp");
            emit0("sti");
        }
        else printf("error in increment/decrement operators\n");
        break;
    }

    case INDEX:
    {
        NODE* indexExp = ptr->son->brother;
        int stIndex;

        if (indexExp->noderep == nonterm) processOperator(indexExp);
        else rv_emit(indexExp);
        stIndex = lookup(ptr->son->token.value.id);
        if (stIndex == -1) {
            printf("undefined variable: %s\n", ptr->son->token.value.id);
            return;
        }
        emit2("lda", symbolTable[stIndex].base, symbolTable[stIndex].offset);
        emit0("add");
        if (!lvalue) emit0("ldi"); // rvalue
        break;
    }

    case CALL:
    {
        NODE* p = ptr->son;     // function name
        char* functionName;
        int stIndex; int noArguments;
        if (checkPredefined(p))  // predefined(Library) functions
            break;

        // handle for user function
        functionName = p->token.value.id;
        stIndex = lookup(functionName);
        if (stIndex == -1) break; // undefined function !!!
        noArguments = symbolTable[stIndex].width;

        emit0("ldp");
        p = p->brother;     // ACTUAL_PARAM
        while (p) {          // processing actual arguemtns
            if (p->noderep == nonterm) processOperator(p);
            else rv_emit(p);
            noArguments--;
            p = p->brother;
        }
        if (noArguments > 0)
            printf("%s: too few actual arguments", functionName);
        if (noArguments < 0)
            printf("%s: too many actual arguments", functionName);
        emitJump("call", ptr->son->token.value.id);
        break;
    }
    } // end switch
}

// nonterm과 terminal에 따라서 처리하는 함수
void processCondition(NODE* ptr)
{
    if (ptr->noderep == nonterm) processOperator(ptr);
    else rv_emit(ptr);
}

// 문장을 처리하는 함수
void processStatement(NODE* ptr)
{
    NODE* p;
    int returnWithValue;

    switch (ptr->token.number) {
    case COMPOUND_ST:
        p = ptr->son->brother; // STAT_LIST
        p = p->son;
        while (p) {
            processStatement(p);
            p = p->brother;
        }
        break;
    case EXP_ST:
        if (ptr->son != NULL) processOperator(ptr->son);
        break;
    case RETURN_ST:
        if (ptr->son != NULL) {
            returnWithValue = 1;
            p = ptr->son;
            if (p->noderep == nonterm)
                processOperator(p); // return value
            else rv_emit(p);
            emit0("retv");
        }
        else
            emit0("ret");
        break;
    case IF_ST:
    {
        char label[LABEL_SIZE];

        genLabel(label);
        processCondition(ptr->son);             // condition part
        emitJump("fjp", label);
        processStatement(ptr->son->brother);    // true part
        emitLabel(label);
    }
    break;
    case IF_ELSE_ST:
    {
        char label1[LABEL_SIZE], label2[LABEL_SIZE];

        genLabel(label1); genLabel(label2);
        processCondition(ptr->son);             // condition part
        emitJump("fjp", label1);
        processStatement(ptr->son->brother);    // true part
        emitJump("ujp", label2);
        emitLabel(label1);
        processStatement(ptr->son->brother->brother); // false part
        emitLabel(label2);
    }
    break;
    case WHILE_ST:
    {
        char label1[LABEL_SIZE], label2[LABEL_SIZE];

        genLabel(label1); genLabel(label2);
        emitLabel(label1);
        processCondition(ptr->son);             // condition part
        emitJump("fjp", label2);
        processStatement(ptr->son->brother);    // loop body
        emitJump("ujp", label1);
        emitLabel(label2);
    }
    break;
    default:
        printf("not yet implemented.\n");
        break;
    } // end switch
}

// 파라미터인 단수 변수를 처리하는 함수
void processSimpleParamVariable(NODE* ptr, int typeSpecifier, int typeQualifier)
{
    NODE* p = ptr->son;     // variable name(=> identifier)
    int stIndex, size;

    if (ptr->token.number != SIMPLE_VAR) printf("error in SIMPLE_VAR\n");

    size = typeSize(typeSpecifier);
    stIndex = insert(p->token.value.id, typeSpecifier, typeQualifier,
        base, offset, 0, 0);
    offset += size;
}

// 파라미터인 배열 변수를 처리하는 함수
void processArrayParamVariable(NODE* ptr, int typeSpecifier, int typeQualifier)
{
    NODE* p = ptr->son; // variable name(=> identifier)
    int stIndex, size;

    if (ptr->token.number != ARRAY_VAR) {
        printf("error in ARRAY_VAR\n");
        return;
    }

    size = typeSize(typeSpecifier);
    stIndex = insert(p->token.value.id, typeSpecifier, typeQualifier,
        base, offset, width, 0);
    offset += size;
}

// 파라미터 선언을 처리하는 함수
void processParamDeclaration(NODE* ptr)
{
    int typeSpecifier, typeQualifier;
    NODE* p, * q;

    if (ptr->token.number != DCL_SPEC) icg_error(6);

    // printf("processParamDeclaration\n");
    // step 1: process DCL_SPEC
    typeSpecifier = INT_TYPE; // default type
    typeQualifier = VAR_TYPE;
    p = ptr->son;
    while (p) {
        if (p->token.number == INT_NODE) typeSpecifier = INT_TYPE;
        else if (p->token.number == CONST_NODE)
            typeQualifier = CONST_TYPE;
        else { // AUTO, EXTERN, REGISTER, FLOAT, DOUBLE, SIGNED, UNSIGEND
            printf("not yet implemented\n");
            return;
        }
        p = p->brother;
    }

    // step 2: process SIMPLE_VAR, ARRAY_VAR
    p = ptr->brother; // SIMPLE_VAR or ARRAY_VAR
    switch (p->token.number) {
    case SIMPLE_VAR: // simple variable
        processSimpleParamVariable(p, typeSpecifier, typeQualifier);
        break;
    case ARRAY_VAR:  // array variable
        processArrayParamVariable(p, typeSpecifier, typeQualifier);
        break;
    default:
        printf("error in SIMPLE_VAR or ARRAY_VAR\n");
        break;
    }
}

// 함수명을 처리하는 함수
void emitFunc(char* FuncName, int operand1, int operand2, int operand3)
{
    int label;
    label = strlen(FuncName);
    fprintf(ucodeFile, "%s", FuncName);
    printf("%s", FuncName);
    for (; label < LABEL_SIZE - 1; label++) {
        fprintf(ucodeFile, " ");
        printf(" ");
    }
    fprintf(ucodeFile, "proc %d %d %d\n", operand1, operand2, operand3);
    printf("proc %d %d %d\n", operand1, operand2, operand3);
}

// 함수헤더를 처리하는 함수
void processFuncHeader(NODE* ptr)
{
    int noArguments, returnType;
    int stIndex;
    NODE* p;

    // printf("processFuncHeader\n");
    if (ptr->token.number != FUNC_HEAD)
        printf("error in processFuncHeader\n");
    // step 1: process the function return type
    p = ptr->son->son;
    while (p) {
        if (p->token.number == INT_NODE) returnType = INT_TYPE;
        else if (p->token.number == VOID_NODE) returnType = VOID_TYPE;
        else printf("invalid function return type\n");
        p = p->brother;
    }

    // step 2: count the number of formal parameters
    p = ptr->son->brother->brother; // FORMAL_PARA
    p = p->son; // PARAM_DCL

    noArguments = 0;
    while (p) {
        noArguments++;
        p = p->brother;
    }

    // step 3: insert the function name
    stIndex = insert(ptr->son->brother->token.value.id, returnType, FUNC_TYPE,
        1/*base*/, 0/*offset*/, noArguments/*width*/, 0/*initialValue*/);
    // if(!strcmp("main", functionName)) mainExist = 1;
}

// 함수를 만드는 것을 처리하는 함수
void processFunction(NODE* ptr)
{
    NODE* p, * q;
    int sizeOfVar = 0;
    int numOfVar = 0;
    int stIndex;

    base++;
    offset = 1;

    if (ptr->token.number != FUNC_DEF) icg_error(4);
    // step 1: process formal parameters
    p = ptr->son->son->brother->brother;
    p = p->son;
    while (p) {
        if (p->token.number == PARAM_DCL) {
            processParamDeclaration(p->son);
            sizeOfVar++;
            numOfVar++;
        }
        p = p->brother;
    }
    // step 2: process the declaration part in function body
    p = ptr->son->brother->son->son;
    while (p) {
        if (p->token.number == DCL) {
            processDeclaration(p->son);
            q = p->son->brother;
            while (q) {
                if (q->token.number == DCL_ITEM) {
                    if (q->son->token.number == ARRAY_VAR) {
                        sizeOfVar += q->son->son->brother->token.value.num;
                    }
                    else sizeOfVar += 1;
                    numOfVar++;
                }
                q = q->brother;
            }
        }
        p = p->brother;
    }

    // step 3: emit the function start code
    p = ptr->son->son->brother;   // IDENT
    emitFunc(p->token.value.id, sizeOfVar, base, 2);
    for (stIndex = symbolTableTop - numOfVar + 1; stIndex < symbolTableTop + 1; stIndex++)
        emitSym(symbolTable[stIndex].base, symbolTable[stIndex].offset, symbolTable[stIndex].width);

    // step 4: process the statement part in function body
    p = ptr->son->brother;   // COMPOUND_ST
    processStatement(p);

    // step 5: check if return type and return value
    p = ptr->son->son;   // DCL_SPEC
    if (p->token.number == DCL_SPEC) {
        p = p->son;
        if (p->token.number == VOID_NODE)   emit0("ret");
        else if (p->token.number == CONST_NODE) {
            if (p->brother->token.number == VOID_NODE)   emit0("ret");
        }
    }

    // step 6: generate the ending codes
    emit0("end");
    base--;
    symbolTable->nextIndex++;
}

// 임시 코드를 생성하는 함수
void codeGen(NODE* ptr)
{
    NODE* p;
    int globalSize; 

    initSymbolTable();
    // step 1: process the declaration part
    for (p = ptr->son; p; p = p->brother) {
        if (p->token.number == DCL) processDeclaration(p->son);
        else if (p->token.number == FUNC_DEF) processFuncHeader(p->son);
        else icg_error(3);
    }

    //dumpSymbolTable();
    globalSize = offset - 1;
    //printf("size of global variables = %d\n", globalSize);

    genSym(base);

    // step 2: process the function part
    for (p = ptr->son; p; p = p->brother)
        if (p->token.number == FUNC_DEF) processFunction(p);
    // if(!mainExist) warningmsg("main does not exist");

    // step 3: generate code for starting routine
    //      bgn     globalSize
    //      ldp
    //      call    main
    //      end
    emit1("bgn", globalSize);
    emit0("ldp");
    emitJump("call", "main");
    emit0("end");
}

/* ********************** main ********************** */

void main(int argc, char* argv[])
{
    //char fileName[30] = "perfect.mc";
    char fileName[30] = "bubble.mc";
    NODE* root;

    printf(" *** start of Mini C Compiler\n");
    // 프롬프트(CMD)에서 실행할 시에 주석제거
    //if (argc != 2) {
    //    icg_error(1);
    //    exit(1);
    //}
    //strcpy(fileName, argv[1]);
    //printf("   * source file name: %s\n", fileName);

    // 파일을 읽는데 없다면 종료
    if ((source_file = fopen(fileName, "r")) == NULL) {
        icg_error(2);
        exit(1);
    }

    // AST와 U-code를 파일로 저장
    astFile = fopen(strcat(strtok(fileName, "."), ".ast"), "w");
    ucodeFile = fopen(strcat(strtok(fileName, "."), ".uco"), "w");

    printf(" === start of Parser\n");
    // 해당 파일을 파서가 파싱후 트리형태인 노드 반환
    root = parser(source_file);
    // 트리형태를 출력
    printTree(root, 1);
    printf(" === start of ICG\n");
    // 트리를 탐색하면서 코드생성
    codeGen(root);
    printf(" *** end of Mini C Compiler\n");

    fclose(source_file);
    fclose(astFile);
    fclose(ucodeFile);
}