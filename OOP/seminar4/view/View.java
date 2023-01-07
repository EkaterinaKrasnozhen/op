package seminar4.view;

import seminar4.presenter.Presenter;

public interface View {
    void start();
    void answer(String m);
    void setPresenter(Presenter presenter);
}
