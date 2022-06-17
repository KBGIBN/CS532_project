import detect
import ocr
import reset

def main():
    detect.detect()
    ocr.extract()
    reset.reset()

if __name__ == '__main__':
    main()