from utils import Utils
from models import Models


def main():
    utils = Utils()  # We call utils
    models = Models()

    data = utils.load_from_csv('in/whr.csv')
    X, y = utils.features_target(data, ['score', 'rank', 'country'], ['score'])
    models.grid_training(X, y)


if __name__=='__main__':
     main()