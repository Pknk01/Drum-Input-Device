//Inpt Pins 2, 5

int A_pin = 2;
int B_Pin = 3;
int C_Pin = 4;
int D_Pin = 5;

void setup()
{
    Serial.begin(9600);

    pinMode(A_pin, INPUT);
    pinMode(B_Pin, INPUT);
    pinMode(C_Pin, INPUT);
    pinMode(D_Pin, INPUT);
}

//Checks which pin is pulled high and outputs index to serial to be read by python script
void loop()
{
    String out = '';

    if(A_pin == HIGH)
        out += 'A'

    if(B_Pin == HIGH)
        out += 'B'
    
    if(C_Pin == HIGH)
        out += 'C'

    if(D_Pin == HIGH)
        out += 'D'

    Serial.println(out + '\n')
}