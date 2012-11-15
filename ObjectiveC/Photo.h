#import <Cocoa/Cocoa.h>

@interface Photo : NSObject {
    NSString* caption;
    NSString* photographer;
}
@property (retain) NSString* caption;       // Macro creates get/set functions
@property (retain) NSString* photographer;

@end
