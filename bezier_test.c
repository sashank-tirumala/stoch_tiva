#include <math.h>
#include "bezier.h"
#include <stdio.h>
#define PI 3.14159
// float action[10] ={0.24504616, -0.11582746,  0.71558934, -0.46091432, -0.36284493,  0.00495828,
//   -0.06466855, -0.45247894,  0.72117291, -0.11068088};
// float action[10] ={-0.05966324,  0.01689064,  0.35201927, -0.10362486, -0.01347287, -0.0224595,
//   0.06660015, -0.60092065,  0.08468813, -0.38072799};
//float action[10] = {0.10764433, -0.22723689,  0.37480827,  0.01160054, -0.18521147,  0.01536253,
//  0.07677522, -0.65195124,  0.0739685,  -0.23965774};

// int main()
// {
//     BezierUpdate(action);
//     float theta = 0;
//     int count =0;

//     printf("leg1_x,leg1_y,leg2_x,leg2_y\n");

//     while(count <1000)
//     {
//         if(theta > 2*PI)
//             {
//                 theta = 0.0;
//             }
//         float xy[4] = {0};
//         BezierInference(theta, xy);
//         theta = theta + (float)PI/100;
//         printf("%f,%f,%f,%f\n", xy[0], xy[1], xy[2], xy[3]);
//         count++;
//     }
// }
