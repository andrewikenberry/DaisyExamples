// Daisy Field Template
#include "daisy_field.h"
#include "daisysp.h"

using namespace daisy;
using namespace daisysp;

DaisyField hw;

void AudioCallback(float *in, float *out, size_t size)
{
    hw.UpdateAllControls();
    
    for (size_t i = 0; i < size; i+=2)
    {
        out[i] = in[i]; 
        out[i+1] = in[i+1];
    }
}

int main(void)
{
    hw.Init();
    hw.StartAdc();
    hw.StartAudio(AudioCallback);

    while(1) {}
}
