const int max = 500;

void main() {
    int i, j, k;
    int rem, sum;

    i = 2;
    while (i <= max) {
        sum = 0;
        k = i / 2;
        j = 1;
        while (j <= max) {
            sum = 0;
            k = i / 2;
            j = 1;
            while (j <= k) {
                rem = i % j;
                if (rem == 0) sum += j;
                ++j;
            }
            if (i == sum)write(i);
            ++i;
        }
    }
}