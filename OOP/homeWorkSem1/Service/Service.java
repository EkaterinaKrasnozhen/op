package homeWorkSem1.Service;

import java.util.Collections;

import homeWorkSem1.FamilyTree;
import homeWorkSem1.Human;

public class Service <T extends Human> {

    public void sortbyName1(FamilyTree<T> humansList) { 
        Collections.sort(humansList.getHumans());
    }

    public void sortById(FamilyTree<T> humansList) {
        Collections.sort(humansList.getHumans(), new HumanComparatorbyId());
    }

    public void sortByAge(FamilyTree<T> humansList) {
        Collections.sort(humansList.getHumans(), new HumanComparatorbyAge());
    }

}
