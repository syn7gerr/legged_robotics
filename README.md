# Legged Robotics

This project is an attempt at producing functional control of a quadruped robot using Dynamixel AX-12+ servos. Onboard processing is performed by a Beaglebone Black. Communication between platforms is handled by ROS. Initial testing is performed by connection over USB.

## Required packages

The pydynamixel library from Ian Danforth is being used. 

https://github.com/iandanforth/pydynamixel

His work is a derivative of the ForestMoon Dynamixel library originally written in C# by Scott Ferguson.

The original license for the C# version is as follows:

This software was written and developed by Scott Ferguson.
The current version can be found at http://www.forestmoon.com/Software/.
This free software is distributed under the GNU General Public License.
See http://www.gnu.org/licenses/gpl.html for details.
This license restricts your usage of the software in derivative works.