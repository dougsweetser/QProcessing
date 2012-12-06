#import "Photo.h"
        
@implementation Photo

@synthesize caption;
@synthesize photographer;

- (void) dealloc
{
    [caption release];        // same as caption.release()
    [photographer release];
    [super dealloc];
}

@end
