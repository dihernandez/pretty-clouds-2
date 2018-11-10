#include <stdlib.h> 
#include <stdio.h>
#include <unistd.h>
#include <opencv2/opencv.hpp>
using namespace cv;

int main(int argc, char** argv )
{
    Mat image;
    unsigned int microseconds = 1000000;
    printf("before imread");
    image = imread("image_holder.jpg", 1);
    printf("after imread \n");
     if ( !image.data )
    {
        printf("No image data \n");
        return -1;
    }
    printf("befoe namedWindow\n");
    namedWindow("Display Image", WINDOW_AUTOSIZE);
    imshow("Display Image", image);
    waitKey(1000);
    destroyAllWindows();
    return 0;
}
