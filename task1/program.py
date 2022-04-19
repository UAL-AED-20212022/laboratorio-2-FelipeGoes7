import encodings
import sys
from views import view
sys.stdout.reconfigure(encoding="utf-8")

if __name__ == "__main__":
    view.main()