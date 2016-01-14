import hashlib

import openslide

class MetadataExtractor:
    PROPERTIES = [
        "objective-power",
        "mpp-x",
        "mpp-y",
        "vendor",
        "width",
        "height",
        "level_count",
        "md5sum",
        "file-location", #From CSV
        "Id"
    ]
    fileMetadata = {}
    def __init__(self, fileMetadata):
        self.fileMetadata = fileMetadata
        self.imageMetadata = self.extractImageMetadata()

    def extractImageMetadata(self):
        fileMetadata = self.fileMetadata
        fileLocation = fileMetadata['file-location']
        try:
            openslideF = openslide.OpenSlide(fileLocation)
            payLoad = openslideF

            return payLoad
        except:
            print("Couldn't read "+parsedInput[key])
        return []

    def generateMD5Checksum(self,fileName):
        m = hashlib.md5()
        blocksize = 2**20
        with open(fileName, "rb") as f:
            while True:
                buf = f.read(blocksize)
                if not buf:
                    break
                m.update(buf)
        return m.hexdigest()



    def createPayLoad(self):
        payLoad = {}
        fileMetadata = self.fileMetadata
        imageMetadata = self.imageMetadata

        for prop in self.PROPERTIES:
            if prop == "file-location":
                payLoad['file-location'] = fileMetadata['file-location']
            elif prop == "Id":
                payLoad['id'] = fileMetadata['id']
            elif prop in ["mpp-x", "mpp-y", "vendor", "objective-power"]:
                payLoad[prop] = imageMetadata.properties['openslide.'+str(prop)]
            elif prop in ["height", "width"]:
                hw = "openslide.level["+str(imageMetadata.level_count - 1)+"]."+str(prop)
                payLoad[prop] = imageMetadata.properties[hw]
            elif prop == "md5sum":
                payLoad[prop] = self.generateMD5Checksum(fileMetadata['file-location'])
            elif prop == "level_count":
                payLoad[prop] = imageMetadata.level_count

            else:
                print("Couldn't handle: "+ prop)
        print(payLoad)
        return payLoad




