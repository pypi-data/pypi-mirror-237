from glue.viewers.common.viewer import Viewer
from glue.viewers.histogram.state import HistogramViewerState
from glue.core.application_base import Application
from glue.core.data import Data


class TestHistogramViewer(Viewer):
    _state_cls = HistogramViewerState


def test_remove_data_collection():

    # Regression test for a bug that caused an IncompatibleAttribute
    # error when updating the number of bins in a histogram after
    # removing a dataset from the DataCollection (this was due to
    # a caching issue)

    data1 = Data(x=[1, 2, 3], label='data1')
    data2 = Data(y=[1, 2, 3], label='data2')

    app = Application()
    app.data_collection.append(data1)
    app.data_collection.append(data2)

    viewer = app.new_data_viewer(TestHistogramViewer)
    viewer.add_data(data1)
    viewer.add_data(data2)

    viewer.state.hist_n_bin = 30

    app.data_collection.remove(data1)

    viewer.state.hist_n_bin = 20


def test_incompatible_datasets():

    # Regression test for a bug that caused an IncompatibleAttribute
    # error when changing the dataset used in the histogram viewer to one that
    # is not linked to the first dataset.

    data1 = Data(x=[1, 2, 3], label='data1')
    data2 = Data(y=[1, 2, 3], label='data2')

    app = Application()
    app.data_collection.append(data1)
    app.data_collection.append(data2)

    viewer = app.new_data_viewer(TestHistogramViewer)
    viewer.add_data(data1)
    viewer.add_data(data2)

    viewer.state.x_att = data1.id['x']

    viewer.state.hist_n_bin = 30

    viewer.state.x_att = data2.id['y']

    viewer.state.hist_n_bin = 20
