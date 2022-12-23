package seminar2;

public abstract class Animal implements Speakable{ //абстрактный, значит не можем сохдать объект
    //public abstract void speak(); { //если тут указали, то в потомках надо реалтзовать. Если implements в астрактном классе - то можно даже метод не прописывать, наследники и так будут обязаны его сделать
    private Writable fw;    
    
    public void save(){

        if (fw != null) {
            fw.save();
        }

        else if (fw instanceof FileWorker) { // делаем проверку относится ли  этому
            FileWorker fileWorker = (FileWorker) fw; //указали явно к чему хотим преобразовать, и тогда получим доступ не только к save и read через интерфейс Writable, а ко всем методам FilWorker
        //но лучше так не делать, теряетя сама идея intarface
        }
    }

    public void setFw(Writable fw) {
        this.fw = fw;
    }

}
