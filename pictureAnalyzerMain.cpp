// #include <stdio.h> 

// int main(int argc, char* argv[]) {

// 	printf("there shall be pictures. \n");

// 	return 0;
// }

#include <stdio.h>
#include <opencv2/opencv.hpp>
using namespace cv;

int main(int argc, char** argv )
{
    if ( argc != 2 )
    {
        printf("usage: DisplayImage.out <image_holder.jpg>\n");
        return -1;
    }
    Mat image;
    image = imread( argv[1], 1 );
     if ( !image.data )
    {
        printf("No image data \n");
        return -1;
    }
    namedWindow("Display Image", WINDOW_AUTOSIZE );
    imshow("Display Image", image);
    waitKey(0);
    return 0;
}