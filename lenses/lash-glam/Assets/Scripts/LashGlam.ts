/**
 * Lash glam face lens.
 *
 * Imitates the "2016 + lashes" and "Lash Light Touch" style lenses from the
 * Lens+ top chart. One lash strip is anchored to each eye. The right-eye copy
 * is the same texture mirrored with flipX, so the pair stays symmetrical.
 *
 * Texture, size, vertical offset and the face index are inputs for tuning in
 * the Inspector.
 */
@component
export class LashGlam extends BaseScriptComponent {
  @input
  lashTexture: Texture;

  @input
  lashSize: number = 0.25;

  @input
  lashOffsetY: number = 0.05;

  @input
  faceIndex: number = 0;

  onAwake() {
    this.createEvent("OnStartEvent").bind(() => this.build());
  }

  private build() {
    if (!this.lashTexture) {
      print("LashGlam: no lash texture assigned");
      return;
    }
    this.addLashes("Left Lashes", AttachmentPointType.LeftEyeballCenter, false);
    this.addLashes("Right Lashes", AttachmentPointType.RightEyeballCenter, true);
  }

  private addLashes(name: string, anchor: AttachmentPointType, mirror: boolean) {
    const anchorObject = global.scene.createSceneObject(`${name} Anchor`);
    anchorObject.setParent(this.sceneObject);
    const head = anchorObject.createComponent("Component.Head") as Head;
    head.faceIndex = this.faceIndex;
    head.setAttachmentPointType(anchor);

    const overlay = global.scene.createSceneObject(name);
    overlay.setParent(anchorObject);
    const image = overlay.createComponent("Component.Image") as Image;
    image.mainPass.baseTex = this.lashTexture;
    image.flipX = mirror;
    overlay.getTransform().setLocalScale(new vec3(this.lashSize, this.lashSize, this.lashSize));
    overlay.getTransform().setLocalPosition(new vec3(0, this.lashOffsetY, 0));
  }
}
